from setuptools import setup

setup(
        name='vite',
        version='1.0.0',
        description='A simple and minimal static site generator.',
        packages='vite'
        entry_points={
            'console_scripts': [
                'vite = vite.cli:main',
                ]
            },
)
