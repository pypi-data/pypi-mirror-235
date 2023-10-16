import pytest
from utils import create_arg_parser, InvalidPathError,parse_args

#NEED TO ADD TESTS WITH ONLY SUMMARY/SEARCH/MTIME PASSED , AN EXCEPTION/ERROR SHOULD BE RAISED
#NEED TO ADD TESTS TO NOT ALLOW MULTIPLE ARGUMENTS AFTER REINDEX

#  fixture for the argument parser.
@pytest.fixture
def parser():
    return create_arg_parser()

def test_no_args(parser):
    """Test with no arguments passed."""
    parsed_args = parser.parse_args([])
    assert parsed_args.reindex is None
    assert parsed_args.search is None
    assert not parsed_args.summary
    assert not parsed_args.mtime
    assert not parsed_args.size

def test_reindex_arg(parser):
    """Test with only --reindex argument passed."""
    parsed_args = parser.parse_args(['--reindex', '/path/to/dir'])
    assert parsed_args.reindex == '/path/to/dir'
    assert parsed_args.search is None

def test_search_arg(parser):
    """Test with only --search argument passed."""
    parsed_args = parser.parse_args(['--search', 'image/jpeg'])
    assert parsed_args.reindex is None
    assert parsed_args.search == 'image/jpeg'

def test_summary_arg(parser):
    """Test with --search and --summary arguments passed."""
    parsed_args = parser.parse_args(['--search', 'image/jpeg', '--summary'])
    assert parsed_args.search == 'image/jpeg'
    assert parsed_args.summary

def test_mtime_arg(parser):
    """Test with --search and --mtime arguments passed."""
    parsed_args = parser.parse_args(['--search', 'image/jpeg', '--mtime'])
    assert parsed_args.search == 'image/jpeg'
    assert parsed_args.mtime

def test_size_arg(parser):
    """Test with --search and --size arguments passed."""
    parsed_args = parser.parse_args(['--search', 'image/jpeg', '--size'])
    assert parsed_args.search == 'image/jpeg'
    assert parsed_args.size

def test_invalid_arg(parser):
    """Test with an invalid argument passed."""
    with pytest.raises(SystemExit):
        parser.parse_args(['--invalidarg'])

def test_empty_path(parser):
    """Test with --reindex argument but without a path."""
    with pytest.raises(SystemExit):
        parser.parse_args(['--reindex'])

def test_invalid_path():
    """Test with an invalid path for the reindex argument."""
    with pytest.raises(InvalidPathError):
        parse_args(['--reindex', '/invalid/path'])
