#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name='tEmplate',
      version='0.1.0',
      description='INSERT TAGLINE HERE.',
      author='Kwpolska',
      author_email='kwpolska@kwpolska.tk',
      url='https://github.com/Kwpolska/tEmplate',
      license='3-clause BSD',
      long_description=open('./docs/README.rst').read(),
      platforms='any',
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=['Development Status :: 1 - Planning'],
      packages=['pkgbuilder'])
      #requires=['stuff'],
      #scripts=['bin/x'],
      #data_files=[('file', ['dest']),],
