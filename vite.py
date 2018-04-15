#!/usr/bin/env python3

"""
Vite - A simple and minimal static site generator.
"""

import sys
import argparse
import pathlib
import os

from huepy import *

usage = lightblue('vite.py') + ' new [PATH]' 
desc = green('A simple and minimal static site generator.')
parser = argparse.ArgumentParser(description=desc, usage=usage)
parser.add_argument(yellow('new'), nargs='*',help='Create new Vite project.')

if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

try:
    args = parser.parse_args()
    project_path = args.new[1]
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
                   os.path.join(abs_path, 'make.py'))
        create_template(path)
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


def create_template(path):
    with open(os.path.join(path, 'templates', 'index.html'), 'w') as f:
        f.write("""
<!DOCTYPE html>
<html>
<header>
	{{ header }}
	<title>
		{{ title }}	
	</title>
</header>

<body>
	{{ body }}
</body>

<footer>
	{{ footer }}
	<p> © {{ author }} </p>
<footer>

                """)


def main():
    if args.new:
        create_project(project_path)

if __name__ == "__main__":
    main()
