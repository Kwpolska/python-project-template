#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import sys
import io
from setuptools import setup, find_packages


setup(name='{{ cookiecutter.repo_name }}',
      version='{{ cookiecutter.version }}',
      description='{{ cookiecutter.project_short_description }}',
      keywords='{{ cookiecutter.repo_name }}',
      author='{{ cookiecutter.full_name }}',
      author_email='{{ cookiecutter.email }}',
      url='https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}',
      license='3-clause BSD',
      long_description=io.open('./docs/README.rst', 'r', encoding='utf-8').read(),
      platforms='any',
      zip_safe=False,
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=['Development Status :: 1 - Planning',
                   'Programming Language :: Python',
                   'Programming Language :: Python :: 2',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3',
                   'Programming Language :: Python :: 3.3',
                   'Programming Language :: Python :: 3.4',
                   'Programming Language :: Python :: 3.5'],
      packages=find_packages(exclude=('tests',)),
      include_package_data=True,
      install_requires=[],
      # data_files=[('file', ['dest']),],
      # entry_points={
           #'console_scripts': [
               #'{{ cookiecutter.repo_name }} = {{ cookiecutter.repo_name }}.__main__:main',
           #]
      # },
      )
