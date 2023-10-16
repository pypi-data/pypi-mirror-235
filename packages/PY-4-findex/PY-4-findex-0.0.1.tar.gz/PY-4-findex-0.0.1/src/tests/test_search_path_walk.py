import pytest
from path_walk import Path_Walk

# Mocking the FileDatabase class's retrieve_mime method
class MockFileDatabase:
    def retrieve_mime(self, mime_type):
        mime_data = {
            "image/jpeg": [{"relative_path": "path1.jpg", "timestamps": 1234567890, "size": 1500}],
            "application/pdf": [{"relative_path": "path2.pdf", "timestamps": 1234567891, "size": 2500}],
        }
        return mime_data.get(mime_type, [])

# Fixture for initializing the Path_Walk class
@pytest.fixture
def path_walk_instance():
    path_walk = Path_Walk()
    path_walk.file_db = MockFileDatabase()  # replacing the actual DB with mock DB
    return path_walk

def test_search_valid_mime_type(path_walk_instance):
    assert path_walk_instance.search("image/jpeg") == [{"relative_path": "path1.jpg", "timestamps": 1234567890, "size": 1500}]

def test_search_invalid_mime_type(path_walk_instance):
    assert path_walk_instance.search("invalid/mime") == []

def test_search_empty_string_mime_type(path_walk_instance):
    assert path_walk_instance.search("") == []

def test_search_pdf_mime_type(path_walk_instance):
    assert path_walk_instance.search("application/pdf") == [{"relative_path": "path2.pdf", "timestamps": 1234567891, "size": 2500}]

