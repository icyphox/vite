import markdown2
import sys
import argparse

parser = argparse.ArgumentParser(description='A simple and mnml static site generator.')
parser.add_argument('new', help='Create a new project.')

if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

args = parser.parse_args()
print(args)
