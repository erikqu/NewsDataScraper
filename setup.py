import sys
import os
import codecs
from setuptools import setup
from os import path


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open("requirements.txt") as f:
    required = f.read().splitlines()
    f.close()

with open("README.md", encoding="utf-8") as f:
    long_description = f.read()


setup(
    name="newsdatascraper",
    version="0.0.2",
    description="Easily query articles",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Erick Torres and Erik Quintanilla",
    author_email="ericktorresdeveloper@gmail.com",
    url="https://github.com/erikqu/NewsDataScraper",
    packages=["newsdatascraper"],
    include_package_data=True,
    install_requires=required,
    license="MIT",
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3.5",
        "Natural Language :: English",
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
    ],
)
