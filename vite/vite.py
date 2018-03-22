#!/usr/bin/env python3

"""
Vite - A simple and minimal static site generator.
"""

import sys
import argparse
import pathlib
import os
import importlib

from hue import *

parser = argparse.ArgumentParser(description="""
        A simple and minimal static site generator.
        """)
parser.add_argument('action', choices=['new', 'build'])
# TODO: add help for each action
parser.add_argument('path', nargs='*')

if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

try:
    args = parser.parse_args()
    project_path = args.path[0]
except IndexError:
    parser.print_help()
    sys.exit(1)


def create_project(path):
    try:
        abs_path = pathlib.Path(path).resolve()
        cur_path = pathlib.Path('.').resolve()
        os.makedirs(os.path.join(path, 'build'))
        os.mkdir(os.path.join(path, 'pages'))
        os.mkdir(os.path.join(path, 'templates'))
        create_config(path)
        os.symlink(os.path.join(cur_path, 'make.py'),
                   os.path.join(abs_path, '.make.py'))
        print(good('Created project directory at %s.' % (abs_path)))
    except FileExistsError:
        print(bad('Error: specified path exists.'))


def create_config(path):
    with open(path + '/config.py', 'w') as f:
        f.write("""# config.py - Vite's configuration script

title = ''
author = ''
header = ''
footer = '' 
template = 'index.html'  # default is index.html
               """)


def build_project(path):
    try:
        os.chdir(path)
        importlib.import_module('make')
    except FileNotFoundError as e:
        print(bad('Error: no such file or directory: %s' % (path)))


def main():
    if args.action == 'new':
        create_project(project_path)
    elif args.action == 'build':
        build_project(project_path)


if __name__ == "__main__":
    main()
