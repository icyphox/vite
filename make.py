#!/usr/bin/env python3

import os
import sys
import jinja2
import time
import argparse

from markdown2 import markdown_path
from huepy import *

desc = green('Script to build and serve Vite projects.')
usage = lightblue('make.py') + ' [serve]'
help_txt = 'Serve pages from the ' + italic('build') + ' directory.'
parser = argparse.ArgumentParser(description=desc, usage=usage)
parser.add_argument('serve', nargs='*', help=help_txt)

# import config file
try:
    sys.path.append(os.getcwd())
    import config
except ModuleNotFoundError:
    print(bad('Error: config.py not found.'))
    print(que('Are you sure you\'re in a project directory?'))
    parser.print_help()
    sys.exit(1)

# constants
PAGES_PATH = 'pages/'
BUILD_PATH = 'build/'
TEMPL_PATH = 'templates/'
TEMPL_FILE = TEMPL_PATH + config.template


# jinja2
def jinja_render(html_text, TEMPL_FILE):
    template_loader = jinja2.FileSystemLoader('./')
    env = jinja2.Environment(loader=template_loader)
    template = env.get_template(TEMPL_FILE)
    output = template.render(title=config.title,
                             author=config.author,
                             header=config.header,
                             footer=config.footer,
                             body=html_text)
    return output


def markdown_render(filename):
    html_text = markdown_path(PAGES_PATH + filename)
    return html_text


def html_gen():
    for page in os.listdir(PAGES_PATH):
        html_text = markdown_render(page)
        html_file= os.path.splitext(os.path.join(BUILD_PATH, page))[0]
        if not os.path.exists(html_file):
            os.mkdir(html_file)
        output = jinja_render(html_text, TEMPL_FILE)
        with open(os.path.join(html_file, 'index.html'), 'w') as f:
            f.write(output)
            print(run('Rendered %s.' % (page)))   


def main():
    start = time.process_time()
    TEMPL_FILE = TEMPL_PATH + config.template
    if not os.listdir(PAGES_PATH):
        print(info(italic('pages') + ' directory is empty. Nothing to build.'))
        sys.exit(1)
    else:
        try:
           html_gen()
           print(info('Done in %0.5fs.' % (time.process_time() - start)))
        except jinja2.exceptions.TemplateNotFound:
           print(bad('Error: specified template not found: %s' % (TEMPL_FILE)))


if __name__ == "__main__":
    main()
