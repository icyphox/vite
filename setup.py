from setuptools import setup

setup(
        name='vite',
        version='1.1',
        description='A simple and minimal static site generator.',
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
