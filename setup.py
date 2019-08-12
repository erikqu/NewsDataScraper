import sys
import os
import codecs


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open("requirements.txt") as f:
    required = f.read().splitlines()
    f.close()


setup(
    name="newsdatascraper",
    version="0.0.1",
    description="Easily query articles",
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
