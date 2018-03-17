from markdown2 import markdown_path
from glob import glob
import os
import sys
import jinja2

# import config file
try:
    sys.path.append(os.getcwd())
    import config
except ImportError:
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
    output = template.render(title=config.title, author=config.author, header=config.header, footer=config.footer, body=html_text)
    return output

def markdown_render(filename):
    html_text = markdown_path(PAGES_PATH + filename)
    return html_text

def main():
    template_file = TEMPL_PATH + '/template.html'
    for page in os.listdir(PAGES_PATH):
        html_text = markdown_render(page)
        html_file = os.path.splitext(page)[0] + '.html'
        output = jinja_render(html_text, template_file)
        with open(BUILD_PATH + html_file, 'w') as f:
            f.write(output)
            print('Rendered %s' % (page))

if __name__ == "__main__":
    main()
