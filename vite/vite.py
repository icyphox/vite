#!/usr/bin/env python3

"""
Vite - A simple and minimal static site generator.
"""

import sys
import pathlib
import os
import jinja2
import time
import http.server
import socketserver

from markdown2 import markdown_path
from huepy import *
from distutils.dir_util import copy_tree
from vite import vite


# constants
PAGES_PATH = 'pages/'
BUILD_PATH = 'build/'
TEMPL_PATH = 'templates/'
TEMPL_FILE = ''
PORT = 1911


def import_config():
    try:
        sys.path.append(os.getcwd())
        globals()['config'] = __import__('config') 
        global TEMPL_FILE
        TEMPL_FILE = os.path.join(TEMPL_PATH, config.template)
    except ImportError:
        print(bad('Error: config.py not found.'))
        print(que('Are you sure you\'re in a project directory?'))
        sys.exit(1)


def create_project(path):
    try:
        abs_path = pathlib.Path(path).resolve()
        cur_path = pathlib.Path('.').resolve()
        os.makedirs(os.path.join(path, 'build'))
        os.mkdir(os.path.join(path, 'pages'))
        os.mkdir(os.path.join(path, 'templates'))
        os.mkdir(os.path.join(path, 'static'))
        create_config(path)
        create_template(path)
        print(good('Created project directory at %s.' % (abs_path)))
    except FileExistsError:
        print(bad('Error: specified path exists.'))


def create_config(path):
    with open(os.path.join(path, 'config.py'), 'w') as f:
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
	<p> {{ author }} </p>
<footer>

                """)

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


def server():
    handler = http.server.SimpleHTTPRequestHandler
    os.chdir(os.path.join(os.getcwd(), BUILD_PATH))
    try:
        with socketserver.TCPServer(('', PORT), handler) as httpd:
            print(run(f'Serving the {italic("build")} directory at http://localhost:{PORT}'))
            print(white('Ctrl+C') + ' to stop.')
            httpd.serve_forever()
    except KeyboardInterrupt:
        print(info('Stopping server.'))
        httpd.socket.close()
        sys.exit(1)

def builder():
    path = os.getcwd()
    start = time.process_time()
    if not os.listdir(os.path.join(path, PAGES_PATH)):
        print(info(italic('pages') + ' directory is empty. Nothing to build.'))
        sys.exit(1)
    else:
        try:
            html_gen()
            if not os.path.exists(os.path.join(path, BUILD_PATH, 'static')):
                os.mkdir(os.path.join(path, BUILD_PATH, 'static'))
            copy_tree('static', os.path.join(path, BUILD_PATH, 'static'))
            print(good('Done in %0.5fs.' % (time.process_time() - start)))
        except jinja2.exceptions.TemplateNotFound:
            print(bad('Error: specified template not found: %s' % TEMPL_FILE))
 