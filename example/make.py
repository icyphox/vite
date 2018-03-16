from markdown2 import markdown_path
from glob import glob
import os

# constants
PAGES_PATH = 'pages/'
BUILD_PATH = 'build/'

for filename in os.listdir(PAGES_PATH):
    html = markdown_path(PAGES_PATH + filename)
    html_file = os.path.splitext(filename)[0] + '.html'
    with open(BUILD_PATH + html_file, 'w') as f:
        f.write(html)
        print('Rendered %s' % (html_file))
        
