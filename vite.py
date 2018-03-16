"""
Vite - A simple and minimal static site generator.
"""

import markdown2
import sys
import argparse
import errno
import pathlib

parser = argparse.ArgumentParser(description='A simple and mnml static site generator.')
parser.add_argument('action', choices=['new'], help='Create a new project.')
parser.add_argument('path', nargs='*')

if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

args = parser.parse_args()
project_path = args.path[0]

def create_dirs(path):
    try:
        pathlib.Path(path + '/pages').mkdir(parents=True, exist_ok=False)
        pathlib.Path(path + '/build').mkdir(exist_ok=False)
    except FileExistsError as e:
        if e.errno != errno.EEXIST:
            raise

def main():
    create_dirs(project_path)


if __name__ == "__main__":
    main()
