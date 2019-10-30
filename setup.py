import sys
import os
import codecs
from setuptools import setup
from os import path


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="newsdatascraper",
    version="0.0.9.1",
    description="Easily query articles",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Erick Torres and Erik Quintanilla",
    author_email="ericktorresdeveloper@gmail.com",
    url="https://github.com/erikqu/NewsDataScraper",
    packages=["newsdatascraper"],
    include_package_data=True,
    install_requires=[
        "requests==2.20.0",
        "httmock==1.3.0",
        "newspaper3k==0.2.8",
        "tests==0.007",
    ],
    license="MIT",
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3.5",
        "Natural Language :: English",
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
    ],
)
