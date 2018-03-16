from markdown2 import markdown_path
from glob import glob
import os
import jinja2

# constants
PAGES_PATH = 'pages/'
BUILD_PATH = 'build/'
TEMPL_PATH = 'templates/'

# jinja2
def jinja_render(html_text, template_file):
    template_loader = jinja2.FileSystemLoader(searchpath=TEMPL_PATH)
    env = jinja2.Environment(loader=template_loader)
    template = env.get_template(template_file)
    output = template.render(body=html_text)
    return output

def markdown_render(filename):
    html_text = markdown_path(PAGES_PATH + filename)
    return html_text

def main():
    template_file = TEMPL_PATH + 'template.html'
    for page in os.listdir(PAGES_PATH):
        html_text = markdown_render(page)
        output = jinja_render(html_text, template_file)
        with open(BUILD_PATH + html_text, 'w') as f:
            f.write(output)
            print('Rendered %s' % (page))
