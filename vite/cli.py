import argparse
import os
import sys
from vite import vite
from huepy import *


def main():
    desc = green('A simple and minimal static site generator.')
    usage = lightblue('vite') + ' [new | build | serve]'
    # parser = argparse.ArgumentParser(description=desc, usage=usage)
    parser = argparse.ArgumentParser()
    # help_text = 'Commands to create, build and serve your project.' 
    sp = parser.add_subparsers(dest='cmd')
    spp = sp.add_parser('new')
    for cmd in ['build', 'serve']:
        sp.add_parser(cmd)
    spp.add_argument('path')
    args = parser.parse_args()

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)
    elif args.cmd == 'new':
        if args.path:
            vite.create_project(args.path)
        else:
            parser.print_help()
    elif args.cmd == 'build':
        vite.builder()
    elif args.cmd == 'serve':
        vite.server()
    else:
        parser.print_help()
