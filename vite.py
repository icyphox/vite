"""
Vite - A simple and minimal static site generator.
"""

import sys
import argparse
import errno
import pathlib
import os
import shutil

parser = argparse.ArgumentParser(description='A simple and mnml static site generator.')
parser.add_argument('action', choices=['new', 'build'])
# TODO: add help for each action
parser.add_argument('path', nargs='*')

if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

args = parser.parse_args()
project_path = args.path[0]

def create_project(path):
    try:
        abs_path = pathlib.Path(path).resolve()
        pathlib.Path(path + '/pages').mkdir(parents=True, exist_ok=False)
        pathlib.Path(path + '/build').mkdir(exist_ok=False)
        shutil.copy('make.py', path)
        print('Created project directory at %s.' % (abs_path))
    except FileExistsError as e:
        print('Error: specified path exists.')

def build_project(path):
    try:
        os.chdir(path)
        import make.py
    except FileNotFoundError as e:
        print('Error: no such file or directory: %s' % (path))

def main():
    if(args.action == 'new'):
        create_project(project_path)
    elif(args.action == 'build'):
        build_project(project_path)

if __name__ == "__main__":
    main()
