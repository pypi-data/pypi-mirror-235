import os
import sys
import tempfile
from unittest.mock import patch
from io import StringIO

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from path_walk import Path_Walk

# Setup a temporary directory for testing
temp_dir = tempfile.mkdtemp()

def test_max_depth():  # test directory with depth greater than max_depth
    path_walk = Path_Walk()
    with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
        path_walk.walk_files(temp_dir, max_depth=2)
        output = mock_stdout.getvalue()
    assert "Total unique thread IDs used:" in output
    assert "Unique thread IDs:" in output

def test_memory_limit(): # test handling a large directory with a memory limit
    path_walk = Path_Walk()
    with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
        path_walk.walk_files(temp_dir, max_files_in_memory=10)
        output = mock_stdout.getvalue()
    assert "Total unique thread IDs used:" in output
    assert "Unique thread IDs:" in output
