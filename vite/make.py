#!/usr/bin/env python3

import os
import sys
import jinja2
import time

from markdown2 import markdown_path
from huepy import *

# import config file
try:
    sys.path.append(os.getcwd())
    import config
except ModuleNotFoundError:
    print(bad('Error: config.py not found.'))

# constants
PAGES_PATH = 'pages/'
BUILD_PATH = 'build/'
TEMPL_PATH = 'templates/'


# jinja2
def jinja_render(html_text, template_file):
    template_loader = jinja2.FileSystemLoader('./')
    env = jinja2.Environment(loader=template_loader)
    template = env.get_template(template_file)
    output = template.render(title=config.title,
                             author=config.author,
                             header=config.header,
                             footer=config.footer,
                             body=html_text)
    return output


def markdown_render(filename):
    html_text = markdown_path(PAGES_PATH + filename)
    return html_text


def main():
    start = time.process_time()
    template_file = TEMPL_PATH + config.template
    try:
        for page in os.listdir(PAGES_PATH):
            html_text = markdown_render(page)
            html_file= os.path.splitext(os.path.join(BUILD_PATH, page))[0]
            if not os.path.exists(html_file):
                os.mkdir(html_file)
            output = jinja_render(html_text, template_file)
            with open(os.path.join(html_file, 'index.html'), 'w') as f:
                f.write(output)
                print(run('Rendered %s.' % (page)))
        print(info('Done in %0.5fs.' % (time.process_time() - start)))
    except jinja2.exceptions.TemplateNotFound:
        print(bad('Error: specified template not found: %s' % (template_file)))


if __name__ == "__main__":
    main()
