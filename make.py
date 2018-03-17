from markdown2 import markdown_path
from glob import glob
import os
import jinja2

# constants
PAGES_PATH = 'pages/'
BUILD_PATH = 'build/'
TEMPL_PATH = 'templates'

# jinja2
def jinja_render(html_text, template_file):
    template_loader = jinja2.FileSystemLoader('./')
    env = jinja2.Environment(loader=template_loader)
    template = env.get_template(template_file)
    output = template.render(title='test', body=html_text)
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
