"""Script for interacting with the database."""
import shelve
from src.exceptions import DatabaseError, MimeTypeError

class FileDatabase:
    """Performs saving and retrieving of files"""
    def __init__(self, db_name = "file_index"):
        self.db_name = db_name
    def save_file(self, file_data, mime_type):
        """
        Storing file_data in an array with key "mime_type"
        For example:
        "image/jpeg":[file_data_1, file_data_2]
        "video/mp4":...
        "application/pdf:..
        """
        # Check if mime_type is a string and is not None
        if not isinstance(mime_type, str) or mime_type is None:
            raise ValueError("MIME type must be a non-empty string")

        # Check if file_data is a dictionary
        if not isinstance(file_data, dict):
            raise ValueError("file_data must be a dictionary")

        try:
            with shelve.open(self.db_name) as database:
                if database.get(mime_type) is not None:
                    temp = database.get(mime_type)
                    if file_data not in temp: # avoid duplicates
                        temp.append(file_data)
                        database[mime_type] = temp
                else:
                    database[mime_type] = [file_data]
        except Exception as error:
            raise DatabaseError(f"Failed to save data in database: {str(error)}") from error

    def retrieve_mime(self,mime_type):
        """Retrieving files in accordance to mime_types"""
        with shelve.open(self.db_name) as database:
            if mime_type in database:
                return database[mime_type]
            raise MimeTypeError(f"Mime type '{mime_type}' does not exist")
