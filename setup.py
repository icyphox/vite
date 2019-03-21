from setuptools import setup
from vite import __version__

with open('README.md') as f:
    long_description = f.read()

setup(
        author='Anirudh',
        author_email='icyph0x@pm.me',
        long_description=long_description,
        long_description_content_type='text/markdown',
        name='vite',
        version=__version__,
        description='A simple and minimal static site generator.',
        url='https://github.com/icyphox/vite',
        license='MIT',
        packages=['vite'],
        install_requires=[
            'markdown2', 'Jinja2', 'huepy', 'pygments',
            ],
        entry_points={
            'console_scripts': [
                'vite = vite.cli:main',
                ]
            },
)
