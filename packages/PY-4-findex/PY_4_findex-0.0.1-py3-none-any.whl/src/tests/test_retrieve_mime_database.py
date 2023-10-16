import pytest
from database import FileDatabase

# Fixture to provide a fresh instance of FileDatabase for each test
@pytest.fixture
def db_instance():
    db = FileDatabase()
    yield db 
    import os
    if os.path.exists("file_index.db"):
        os.remove("file_index.db")

# Test 1: Retrieving a known mime type
def test_retrieve_known_mime(db_instance):
    db_instance.save_file({"relative_path": "sample.jpg"}, "image/jpeg")
    result = db_instance.retrieve_mime("image/jpeg")
    assert result == [{"relative_path": "sample.jpg"}]

# Test 2: Retrieving an unknown mime type
def test_retrieve_unknown_mime(db_instance):
    with pytest.raises(Exception, match="This mime_type does not exist"):
        db_instance.retrieve_mime("unknown/mime")

# Test 3 Retrieving with an empty string as mime type
def test_retrieve_empty_mime(db_instance):
    with pytest.raises(Exception, match="This mime_type does not exist"):
        db_instance.retrieve_mime("")

# Test 4: Retrieving with a very long string
def test_retrieve_long_mime(db_instance):
    with pytest.raises(Exception, match="This mime_type does not exist"):
        db_instance.retrieve_mime("a" * 1000)

# Test 5: Retrieve after adding multiple data for same mime
def test_retrieve_multiple_data_same_mime(db_instance):
    db_instance.save_file({"relative_path": "sample2.jpg"}, "image/jpeg")
    result = db_instance.retrieve_mime("image/jpeg")
    assert len(result) == 1

# Test 6: Testing database with large file entry
def test_large_file_entry(db_instance):
    large_data = {"relative_path": "a" * 10000}
    db_instance.save_file(large_data, "image/large")
    result = db_instance.retrieve_mime("image/large")
    assert result == [large_data]

# Test 7: Retrieve data after multiple additions
def test_retrieve_after_multiple_additions(db_instance):
    db_instance.save_file({"relative_path": "sample3.jpg"}, "image/png")
    db_instance.save_file({"relative_path": "sample4.jpg"}, "image/gif")
    result = db_instance.retrieve_mime("image/gif")
    assert result == [{"relative_path": "sample4.jpg"}]

# Test 8: Retrieve mime with special characters
def test_retrieve_mime_special_characters(db_instance):
    mime_type = "image/jpg; charset=utf-8"
    db_instance.save_file({"relative_path": "sample5.jpg"}, mime_type)
    result = db_instance.retrieve_mime(mime_type)
    assert result == [{"relative_path": "sample5.jpg"}]

