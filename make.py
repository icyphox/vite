from markdown2 import markdown_path
from glob import glob
import os

# constants
PAGES_PATH = 'pages/'
BUILD_PATH = 'build/'

for filename in os.listdir(PAGES_PATH):
    html = markdown_path(PAGES_PATH + filename)
    with open(BUILD_PATH + filename + '.html', 'w') as f:
        f.write(html)
        
