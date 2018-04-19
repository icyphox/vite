import argparse
import os

from vite import vite
from huepy import *


def main():
    desc = green('A simple and minimal static site generator.')
    usage = lightblue('vite') + ' [new | build | serve]'
    parser = argparse.ArgumentParser(description=desc, usage=usage)
    help_text = 'Commands to create, build and serve your project.' 
    parser.add_argument('action', choices=['new', 'build', 'serve'], help=help_text)
    parser.add_argument('path', nargs='*')

    project_path = args.path[0]
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)
    elif args.new:
        vite.create_project(project_path)
    elif args.build:
        vite.builder()
    elif args.serve:
        vite.server()
    else:
        parser.print_help()

if args.new:
    vite.create_project(project_path)
