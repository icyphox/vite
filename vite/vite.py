#!/usr/bin/env python3

"""
Vite - A simple and minimal static site generator that JustWorks™
Author: Anirudh <icyph0x@pm.me>
License: MIT
"""

import sys
import pathlib
import os
import jinja2
import time
import http.server
import socketserver
import shutil

from markdown2 import markdown_path
from huepy import *


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
        f.write("""<!DOCTYPE html>
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
def jinja_render(html_text, tmpl):
    template_loader = jinja2.FileSystemLoader('./')
    env = jinja2.Environment(loader=template_loader)
    try:
        template = env.get_template(tmpl)    
        output = template.render(title=config.title,
                             author=config.author,
                             header=config.header,
                             footer=config.footer,
                             body=html_text)
        return output
    except jinja2.exceptions.TemplateNotFound:
        print(bad('Error: specified template not found: %s' % (tmpl)))
        sys.exit(1)


def fm_template(metadata):
    try:
        page_template = os.path.join(os.path.join(TEMPL_PATH, metadata['template']))
    except KeyError:
        page_template = TEMPL_FILE
    return page_template


def markdown_render(filename):
    html_text = markdown_path(os.path.join(PAGES_PATH, filename), extras=['metadata'])
    return html_text


def html_gen():
    def index_render(f, d=''):
        index_html = markdown_render(os.path.join(d, f))
        output = jinja_render(index_html, fm_template(index_html.metadata))
        with open(os.path.join(BUILD_PATH, d, 'index.html'), 'w') as ff:
            ff.write(output)
            if d:
                print(run('Rendered ' + white('%s/%s') % (d, f)))
            else:
                print(run('Rendered ' + white('%s') % (f)))

    def normal_render(f, d=''):
        html_text = markdown_render(os.path.join(d, f))
        html_file = os.path.splitext(os.path.join(BUILD_PATH, d, f))[0]
        os.mkdir(html_file)
        output = jinja_render(html_text, fm_template(html_text.metadata))
        with open(os.path.join(html_file, 'index.html'), 'w') as ff:
            ff.write(output)
            if d:
                print(run('Rendered ' + white('%s/%s') % (d, f)))
            else:
                print(run('Rendered ' +  white('%s') % (f)))


    for root, dirs, files in os.walk(PAGES_PATH):
        for d in dirs:
            os.mkdir(os.path.join(BUILD_PATH, d))
            for f in os.listdir(os.path.join(PAGES_PATH, d)):
                if os.path.splitext(f)[1] != '.md':
                    shutil.copyfile(os.path.join(PAGES_PATH, d, f),
                                    os.path.join(BUILD_PATH, d, f))
                    print(run('Copied ' + white('%s/%s') % (d, f)))
                elif f == '_index.md':
                    index_render(f, d)
                else:
                    normal_render(f, d)

    for f in os.listdir(PAGES_PATH):
        if os.path.isfile(os.path.join(PAGES_PATH, f)):
            if os.path.splitext(f)[1] != '.md':
                shutil.copyfile(os.path.join(PAGES_PATH, f), os.path.join(BUILD_PATH, f))
                print(run('Copied ' + white('%s') % (f)))
            elif f == '_index.md':
                index_render(f)
            else:
                normal_render(f)


def server():
    handler = http.server.SimpleHTTPRequestHandler
    os.chdir(os.path.join(os.getcwd(), BUILD_PATH))
    try:
        with socketserver.TCPServer(('', PORT), handler) as httpd:
            print(run(f'Serving the {italic(cyan("build"))} directory at {yellow(f"http://localhost:{PORT}")}'))
            print(white('Ctrl+C') + ' to stop.')
            httpd.serve_forever()
    except KeyboardInterrupt:
        print(info('Stopping server.'))
        httpd.socket.close()
        sys.exit(1)


def clean():
    shutil.rmtree(BUILD_PATH)
    os.makedirs(BUILD_PATH)


def builder():
    path = os.getcwd()
    start = time.process_time()
    if not os.listdir(os.path.join(path, PAGES_PATH)):
        print(info(italic('pages') + ' directory is empty. Nothing to build.'))
        sys.exit(1)
    else:
        clean()
        html_gen()
        if os.path.exists(os.path.join(os.getcwd(), 'static')):
            shutil.copytree(os.path.join(os.getcwd(), 'static'), os.path.join(BUILD_PATH, 'static'))
        print(good('Done in %0.5fs.' % (time.process_time() - start)))
