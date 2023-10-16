import pytest
from utils import parse_args
from exceptions import InvalidPathError

def test_valid_reindex_path():
    result = parse_args(['--reindex', '.'])  # Assuming current directory exists
    assert result.reindex == '.'

def test_invalid_reindex_path():
    with pytest.raises(InvalidPathError):
        parse_args(['--reindex', '/nonexistentpath'])
