"""
Utility functions for the file index and search tool.
"""

import os
import argparse
from src.exceptions import InvalidPathError

def create_arg_parser():
    """
    Creates and returns the command-line argument parser.
    """
    parser = argparse.ArgumentParser(description='File index and search tool.')
    parser.add_argument('--reindex',
                        metavar='PATH',
                        help='Create an index from the given path.'
                        )
    parser.add_argument('--search',
                        metavar='MIME_TYPE',
                        help='MIME type to search (e.g. image/jpeg)'
                        )
    parser.add_argument('--summary',
                        action='store_true',
                        help='Print a summary of the matched files.'
                        )
    parser.add_argument('--mtime',
                        action='store_true',
                        help='Print modification timestamp of each file.'
                        )
    parser.add_argument('--size', action='store_true', help='Print size of each file.')

    return parser

def parse_args(args=None):
    """
    Parses command-line arguments and handles exceptions.
    """
    parser = create_arg_parser()
    parsed_args = parser.parse_args(args)

    # Handle invalid path for reindex
    if parsed_args.reindex and not os.path.exists(parsed_args.reindex):
        raise InvalidPathError(f"The provided path '{parsed_args.reindex}' does not exist.")

    # Check if --search is used without any of the optional arguments
    if not parsed_args.search and (parsed_args.summary or parsed_args.mtime or parsed_args.size):
        raise ValueError("--summary, --mtime, and --size options require --search to be specified.")

    return parsed_args
