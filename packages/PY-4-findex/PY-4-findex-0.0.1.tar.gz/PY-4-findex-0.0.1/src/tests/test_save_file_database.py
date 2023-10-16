import pytest
from database import FileDatabase

# Fixture for initializing the database
@pytest.fixture
def file_db():
    return FileDatabase(DB_NAME="test_db")

# Cleanup function to delete the test database after each test
def teardown_function():
    """Cleanup after each test."""
    import os
    if os.path.exists("test_db.db"):
        os.remove("test_db.db")

# Test if a single entry is stored correctly
def test_save_file_single_entry(file_db):
    data = {
        'relative_path': 'path/to/file.jpg',
        'timestamps': 1633372000,
        'permissions': 755,
        'ownership': 1001,
        'size': 1024
    }
    mime_type = "image/jpeg"
    file_db.save_file(data, mime_type)
    retrieved_data = file_db.retrieve_mime(mime_type)
    assert len(retrieved_data) == 1
    assert retrieved_data[0]['relative_path'] == data['relative_path']

# Test if multiple entries with the same MIME type are stored correctly
def test_save_file_multiple_entries_same_mime(file_db):
    data1 = {'relative_path': 'path/to/file1.jpg', 'size': 1024}
    data2 = {'relative_path': 'path/to/file2.jpg', 'size': 2048}
    mime_type = "image/jpeg"
    file_db.save_file(data1, mime_type)
    file_db.save_file(data2, mime_type)
    retrieved_data = file_db.retrieve_mime(mime_type)
    assert len(retrieved_data) == 2
    assert retrieved_data[1]['relative_path'] == data2['relative_path']

# Test if multiple entries with different MIME types are stored correctly
def test_save_file_multiple_entries_different_mime(file_db):
    data1 = {'relative_path': 'path/to/file1.jpg', 'size': 1024}
    data2 = {'relative_path': 'path/to/file2.mp4', 'size': 2048}
    mime_type1 = "image/jpeg"
    mime_type2 = "video/mp4"
    file_db.save_file(data1, mime_type1)
    file_db.save_file(data2, mime_type2)
    assert len(file_db.retrieve_mime(mime_type1)) == 1
    assert len(file_db.retrieve_mime(mime_type2)) == 1

# Test if the same data can be stored multiple times
def test_save_file_overwrite_same_data(file_db):
    data = {'relative_path': 'path/to/file.jpg', 'size': 1024}
    mime_type = "image/jpeg"
    file_db.save_file(data, mime_type)
    file_db.save_file(data, mime_type)
    retrieved_data = file_db.retrieve_mime(mime_type)
    assert len(retrieved_data) == 1

# Test storing an empty data dictionary
def test_save_file_empty_data(file_db):
    data = {}
    mime_type = "image/jpeg"
    with pytest.raises(Exception, match="This mime_type does not exist"):
        file_db.save_file(data, mime_type)
        file_db.retrieve_mime("non-existent-mime")

# Test retrieving a MIME type without saving anything
def test_save_file_no_data(file_db):
    with pytest.raises(Exception, match="This mime_type does not exist"):
        file_db.retrieve_mime("image/jpeg")

# Test saving with an invalid MIME type (integer instead of string)
def test_save_file_invalid_mime_type():
    db = File_DB()
    file_data = {'relative_path': 'path/to/file.jpg', 'size': 1024}
    mime_type = 12345  # This is an invalid MIME type
    
    with pytest.raises(ValueError, match="MIME type must be a non-empty string"):
        db.save_file(file_data, mime_type)

# Test saving a large entry
def test_save_file_large_data(file_db):
    data = {'relative_path': 'a'*10000, 'size': 1024}
    mime_type = "image/jpeg"
    file_db.save_file(data, mime_type)
    retrieved_data = file_db.retrieve_mime(mime_type)
    assert len(retrieved_data) == 1
    assert len(retrieved_data[0]['relative_path']) == 10000

# Test saving data in an invalid format (string instead of dict)
def test_save_file_invalid_data_format(file_db):
    data = "invalid_format"
    mime_type = "image/jpeg"
    with pytest.raises(Exception):
        file_db.save_file(data, mime_type)
