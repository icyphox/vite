from markdown2 import markdown_path
from glob import glob
import os
import jinja2

# constants
PAGES_PATH = 'pages/'
BUILD_PATH = 'build/'
TEMPL_PATH = 'templates/'

# jinja2
def jinja_render(markdown_text, template_file):
    template_loader = jinja2.FileSystemLoader(searchpath=TEMPL_PATH)
    env = jinja2.Environment(loader=template_loader)
    template = env.get_template(template_file)
    output = template.render(body=markdown_text)
    return output
