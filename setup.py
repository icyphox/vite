from setuptools import setup

with open('README.md') as f:
    long_description = f.read()

setup(
        author='Anirudh',
        author_email='icyph0x@pm.me',
        long_description=long_description,
        long_description_content_type='text/markdown',
        name='vite',
        version='1.2',
        description='A simple and minimal static site generator.',
        url='https://github.com/icyphox/vite',
        packages=['vite'],
        install_requires=[
            'markdown2', 'Jinja2', 'huepy',
            ],
        entry_points={
            'console_scripts': [
                'vite = vite.cli:main',
                ]
            },
)
