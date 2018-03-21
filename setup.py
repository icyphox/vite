import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
        name = 'Vite',
        version = '1.0.0',
        author = 'Anirudh Oppiliappan',
        author_email = 'icyph0x@protonmail.com',
        description = ('A simple and minimal static site generator.'),
        license = 'MIT',
        url = 'https://github.com/icyphox/vite',
        packages = ['vite'],
        install_requires = [
            'markdown2',
        ],
        zip_safe=False)
