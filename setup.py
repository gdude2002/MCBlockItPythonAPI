# coding=utf-8
import distribute_setup
distribute_setup.use_setuptools()

from setuptools import setup, find_packages
setup(
    name = "MCBlockIt API",
    version = "0.1a1",
    packages = find_packages('src'),
    scripts = ['mcblockit.py'],

    package_data = {
        '': ['src'],
        },

    # metadata for upload to PyPI
    author = "Gareth Coles",
    author_email = "gdude2002@pageserved.com",
    description = "This package provides access to the MCBlock.it API. " \
                  "Please see the GitHub for more information.",
    license = "BSD-3",
    keywords = "api mcblockit mcblock mcblock.it",
    url = "https://github.com/gdude2002/MCBlockItPythonAPI",

    # could also include long_description, download_url, classifiers, etc.
)