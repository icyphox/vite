"""
Vite - A simple and minimal static site generator.
"""

import markdown2
import sys
import argparse
import os
import errno

parser = argparse.ArgumentParser(description='A simple and mnml static site generator.')
parser.add_argument('action', choices=['new'], help='Create a new project.')
parser.add_argument('path', nargs='*')

if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

args = parser.parse_args()
project_path = args.path[0]

try:
    os.makedirs(project_path)
    os.makedirs(project_path + '/pages')
    os.makedirs(project_path + '/build')
    print('Created project directory at %s.' % (project_path))
except OSError as e:
    if e.errno != errno.EEXIST:
        raise
