import os
import magic
from tqdm import tqdm
from src.database import FileDatabase
from src.exceptions import InvalidPathError, DatabaseStorageError
import concurrent.futures
import threading

class Path_Walk:
    def __init__(self):
        self.file_db = FileDatabase()
        self.unique_thread_ids = set()  # To store unique thread IDs

    def process_file(self, full_path, path, i, pbar):
        thread_id = threading.get_ident()  # Get each unique thread ID
        self.unique_thread_ids.add(thread_id)  # Add the thread ID to the set

        if not os.access(full_path, os.R_OK):  # Check if the current thread has 'Read' permission for the file
            with self.permission_issues_lock:
                self.permission_issues.append(full_path)
            return

        relative_path = os.path.relpath(full_path, path)
        immediate_folder = os.path.basename(os.path.dirname(full_path))
        file_display = f"{immediate_folder}/{os.path.basename(full_path)}"

        mime_type = magic.from_file(full_path, mime=True)

        stats = os.stat(full_path)
        file_data = {
            'relative_path': relative_path,
            'timestamps': stats.st_mtime,
            'permissions': stats.st_mode,
            'ownership': stats.st_uid,
            'size': stats.st_size
        }

        self.file_db.save_file(file_data, mime_type)
        pbar.set_postfix(file=file_display, refresh=False)
        pbar.update(1)

    def walk_files(self, path, max_depth=10, max_files_in_memory=6500):
        path = path.strip()
        if not os.path.exists(path):
            raise InvalidPathError(f"The provided path '{path}' does not exist.")

        self.permission_issues = []
        self.permission_issues_lock = threading.Lock() #providing thread safety for concurrent access

        if os.path.exists("file_index.db"):
            os.remove("file_index.db")

        total_files = 0
        for root, dirs, files in os.walk(path): #max_depth - prevents the model from getting stuck in an infinite loop
            if max_depth is not None and root.count(os.sep) - path.count(os.sep) >= max_depth: 
                del dirs[:] # delete all elements in the 'dirs' list beyond maximum depth.
                continue
            total_files += len([file_name for file_name in files if not file_name.startswith('.')])

        # if total_files > 7000: #storage limit is 7000 in database
        #     raise DatabaseStorageError("Too many files. Out of storage in the database.") 

        bar_format = "\033[96m{desc}\033[0m: {percentage:3.0f}%| \033[92m{bar}\033[0m {n_fmt}/{total_fmt} files indexed {postfix}  , [{elapsed} : time elapsed ,{remaining} : remaining ] "
        with tqdm(total=total_files, desc="Indexing", dynamic_ncols=True, bar_format=bar_format) as pbar:
            i = 1
            processed_files = 0  
            file_data_buffer = []

            with concurrent.futures.ThreadPoolExecutor() as executor:
                for root, dirs, files in os.walk(path):
                    dirs[:] = [d for d in dirs if not d.startswith('.')]
                    for file_name in files:
                        if file_name.startswith('.'):
                            continue
                        full_path = os.path.join(root, file_name)

                        if max_files_in_memory is not None: #prevents crashing in out of memory conditions
                            if len(file_data_buffer) >= max_files_in_memory:
                                self.process_file_batch(file_data_buffer, pbar) #processes files in batches instead
                                file_data_buffer = []

                        file_data = {
                            'full_path': full_path,
                            'path': path,
                            'i': i,
                            'pbar': pbar
                        }
                        file_data_buffer.append(file_data)
                        processed_files += 1
                        i += 1

            if max_files_in_memory is not None and file_data_buffer:
                self.process_file_batch(file_data_buffer, pbar)

        if self.permission_issues:
            print("\nFiles with permission issues:")
            for file in self.permission_issues:
                print(file)

        print(f"Total unique thread IDs used: {len(self.unique_thread_ids)}")
        print(f"Unique thread IDs: {', '.join(map(str, self.unique_thread_ids))}")

    def process_file_batch(self, file_data_batch, pbar): # batch-processing for when large number of files
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = []
            for file_data in file_data_batch:
                futures.append(executor.submit(self.process_file, **file_data))
            concurrent.futures.wait(futures)


    def search(self, mime_type):
        files_mime = self.file_db.retrieve_mime(mime_type)
        return files_mime

    def search_pprint(self, mime_type, summary=False, mtime=False, size=False):
        files_mime = self.search(mime_type)

        if summary==True:
            total_files = len(files_mime)
            total_bytes = sum([file["size"] for file in files_mime])
            print(f"Total files: {total_files}. Total size: {total_bytes} bytes.")

        else:
            for file in files_mime:
                suffix = ""
                if mtime==True:
                    suffix += f"\tModification Time: {file['timestamps']}"
                if size==True:
                    suffix += f"\tSize: {file['size']} bytes"
                print(f"./{file['relative_path']}" + suffix)


