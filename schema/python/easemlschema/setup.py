# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages
from easemlschema import __version__

with open("README.md", "r") as fh:
    README = fh.read()

# The main source of truth for install requirements of this project is the requirements.txt file.
with open("requirements.txt", "r") as f:
    REQUIREMENTS = f.readlines()

setup(
    name='easemlschema',
    version=__version__,
    description='Schema which is used to define the type of a machine learning data set.',
    long_description=README,
    long_description_content_type="text/markdown",
    author='Bojan Karlas',
    author_email='bojan.karlas@gmail.com',
    url='https://github.com/DS3Lab/easeml',
    license='MIT',
    install_requires=REQUIREMENTS,
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ]
)
