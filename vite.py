"""
Vite - A simple and minimal static site generator.
"""

import sys
import argparse
import errno
import pathlib
import os

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
        cur_path = pathlib.Path('.').resolve()
        pathlib.Path(path + '/pages').mkdir(parents=True, exist_ok=False)
        pathlib.Path(path + '/build').mkdir(exist_ok=False)
        pathlib.Path(path + '/templates').mkdir(exist_ok=False)
        create_config(path)
        os.symlink(cur_path / 'make.py', abs_path / 'make.py')
        print('Created project directory at %s.' % (abs_path))
    except FileExistsError as e:
        print('Error: specified path exists.')

def create_config(path):
    with open(path + '/config.py', 'w') as f:
        f.write("""# config.py - Vite's configuration script

title = ''
author = ''
header = ''
footer = ''
               """)

def build_project(path):
    try:
        sys.path.append(path)
        os.chdir(path)
        import make
    except FileNotFoundError as e:
        print('Error: no such file or directory: %s' % (path))

def main():
    if(args.action == 'new'):
        create_project(project_path)
    elif(args.action == 'build'):
        build_project(project_path)

if __name__ == "__main__":
    main()
