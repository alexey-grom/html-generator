#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='htmlgenerator',
    version='0.1',
    description='Pythonic html generator',
    author='Alexey Gromov',
    author_email='alxgrmv@gmail.com',
    url='https://github.com/alexey-grom/html-generator',
    packages=find_packages(),
    install_requires=['six', ],
)
