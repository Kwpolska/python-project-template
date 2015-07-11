#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import sys
import io
from setuptools import setup
from setuptools.command.test import test as TestCommand

with open('requirements.txt', 'r') as fh:
    dependencies = [l.strip() for l in fh]

class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = ['tests/']
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)

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
      cmdclass={'test': PyTest},
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=['Development Status :: 1 - Planning',
                   'Programming Language :: Python',
                   'Programming Language :: Python :: 2',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3',
                   'Programming Language :: Python :: 3.3',
                   'Programming Language :: Python :: 3.4'],
      packages=['{{ cookiecutter.repo_name }}'],
      install_requires=dependencies,
      #requires=['stuff'],
      #data_files=[('file', ['dest']),],
      #entry_points={
          #'console_scripts': [
              #'{{ cookiecutter.repo_name }} = {{ cookiecutter.repo_name }}.__main__:main',
          #]
      #},
      )
