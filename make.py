from markdown2 import markdown_path
import os
import sys
import jinja2
import importlib

# import config file
try:
    sys.path.append(os.getcwd())
    importlib.import_module('config')
except ModuleNotFoundError:
    print('Error: config.py not found')

# constants
PAGES_PATH = 'pages/'
BUILD_PATH = 'build/'
TEMPL_PATH = 'templates'


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
    template_file = TEMPL_PATH + '/index.html'
    for page in os.listdir(PAGES_PATH):
        html_text = markdown_render(page)
        html_path = os.path.splitext(os.path.join(BUILD_PATH, page))[0]
        if not os.path.exists(html_path):
            os.mkdir(html_path)
        output = jinja_render(html_text, template_file)
        with open(os.path.join(html_path, 'index.html'), 'w') as f:
            f.write(output)
            print('Rendered %s' % (page))


if __name__ == "__main__":
    main()
