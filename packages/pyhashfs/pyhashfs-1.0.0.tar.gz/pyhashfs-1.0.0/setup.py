#!python
"""A setuptools based setup module.

ToDo:
- Everything
"""

import setuptools

import simplifiedapp

import hashfs

setuptools.setup(**simplifiedapp.object_metadata(hashfs))
