#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='orange_support',
    version='1.0',
    author='Alexander Petrov',
    author_email='apetrov@hey.com',
    url='https://github.com/apetrov/orange_support',
    packages=find_packages(),  # Use find_packages to automatically find all packages
    install_requires=[
        'numpy',
        'pandas',
        'pymc',
        'matplotlib',
        'seaborn',
        'arviz'
    ],
)
