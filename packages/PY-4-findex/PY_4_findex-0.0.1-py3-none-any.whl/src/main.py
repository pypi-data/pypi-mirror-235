#!/usr/bin/env python

"""
Script for performing file indexing and searching operations
"""

import os
import sys
os.chdir('../')
current_directory = os.getcwd()
sys.path.append(current_directory)
from src.utils import parse_args
from src.path_walk import Path_Walk

def main():
    """Parsing command line arguments and performing file indexing and searching operations"""
    try:
        # Parse command line arguments
        parsed_args = parse_args()

        if len(sys.argv) == 1:
            parsed_args.parser.print_help()
            sys.exit(1)

        path_walk = Path_Walk()

        if parsed_args.reindex:
            path = parsed_args.reindex
            path_walk.walk_files(path)

        elif parsed_args.search:
            path_walk.search_pprint(
                parsed_args.search,
                parsed_args.summary,
                parsed_args.mtime,
                parsed_args.size
                )
    except Exception as e: # pylint: disable=broad-except
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) == 1:
        sys.argv.append('--help')
    main()
