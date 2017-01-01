===============================================
Python Project Template.  INSERT TAGLINE HERE.™
===============================================
:Info: This is the README file for the Python Project Template.
:Author: Chris Warrick <chris@chriswarrick.com>
:Copyright: © 2013-2017, Chris Warrick.
:Date: 2017-01-01
:Version: 2.1.2

.. index: README
.. image:: https://travis-ci.org/Kwpolska/python-project-template.svg?branch=master

USING THE TEMPLATE
------------------

Requirements
============

* ``zsh`` installed (required by ``/release`` and ``/.pypt/localegen`` scripts)
* Python with ``cookiecutter`` (initial generation), ``requests`` (required by ``/.pypt/{commitlog,ghrel}``) and ``twine`` (required by ``/release``) installed
* A git repository.  The PyPT is ready to go if you use GitHub.  If you do not
  want GitHub, edit the ``/PKGBUILD{,-2}{,-git}`` files and any other places
  where GitHub is mentioned, including this document which you should edit
  mentally.
* PGP/GPG setup (for signing release commits and tags)
* Travis CI account (if you do not want Travis CI, remove ``/.travis.yml``)

Contents
========

The template contains the following files to get you started:

* pre-configured Sphinx with:

  * ``CONTRIBUTING.rst`` guide (used by GitHub when sending a pull request or an issue)
  * ``LICENSE.rst``
  * an empty ``CHANGELOG.rst``
  * ``README.rst``
  * a bare-bones ``index.rst`` page

* The exact same files in ``/``, which are fragile and **MAY NOT** be modified
  as they are replaced with copies in ``/docs`` by the ``release``
  script
* ``__init__.py`` and ``template.py`` files in the Python package directory
* A ``setup.py`` file that could be good enough for people, and that supports
  ``entry_points`` (see https://go.chriswarrick.com/entry_points).
* ``tests/`` containing some *Is My Python Sane?*-style tests (using ``py.test``)
* An automated global update script (``.pypt/PYPT-UPDATE``)
* Entry points configuration ready to be uncommented
* Addons for Qt users (in ``pypt-extras/``)
* A sample hook for AUR updates (in ``pypt-extras``)
* PKGBUILDs for the Arch Linux User Repository (AUR)
* A state-of-the-art ``release`` script, the operations of which are:

  * querying the user for version number
  * updating ``/docs/CHANGELOG.rst``
  * bumping the version number in all the files, changing dates where necessary
  * copying over ``/docs/README.rst``,  ``/docs/CHANGELOG.rst`` and ``/docs/CONTRIBUTING.rst`` to ``/``
  * locale generation (via the ``.pypt/localegen`` script)
  * running ``import $PROJECTLC`` and the testsuite
  * uploading a source distribution and a wheel to PyPI
  * committing into git and tagging
  * creating a GitHub Releases entry
  * with hooks, updating the AUR package

Getting up to speed in 12 easy steps
====================================

1. Create the repository for the project on GitHub and enable it on Travis CI.
2. Run ``cookiecutter``.
3. Modify all documents: match under/overlines, write real content.
4. Copy: (when using the included ``release`` script, it happens automatically)

   1. ``/docs/README.rst`` to ``/README.rst`` and ``/README``
   2. ``/docs/CHANGELOG.rst`` to ``/CHANGELOG.rst``

5. Modify ``/.pypt/config``, if needed.
6. Generate a `GitHub Personal Access Token <https://github.com/settings/tokens>`_
   in the ``repo`` scope and write it to a ``/.pypt/gh-token`` file. You may
   reuse tokens between different repos running PyPT.
7. Customize ``/setup.py`` to your liking.  You should pay attention to the
   classifiers and the commented-out parts.
8. Customize ``requirements.txt``.
9. If you are using PyQt or PySide, make sure to put your UI code in a ``ui``
    submodule.  Copy the ``pypt-extras/Qt/resources.py`` file to that
    submodule, even if you are not using resources now. Make sure to create a
    ``.pro`` file with your sources and locales. If you want to use the AUR
    package updater, copy the hook to ``.pypt/hooks`` (change its name) and
    modify it to fit your AUR workflow.
10. Remove the ``pypt-extras`` directory if you don’t need anything else from it.
11. If you have a ``PYPT-UPDATE`` script, add your new project to the list
    there.  If not, you may want to copy it from the repository root and set it up.
12. Run the following commands::

        source .pypt/config
        git init
        git remote add origin git@github.com:$GITUSER/$GITREPO
        git add *
        git commit -sm 'initial commit via @Kwpolska’s Python Project Template'
        git push -u origin master

COPYRIGHT
---------

Python Project Template is licensed under a BSD-like license.  You are free to
relicense your code to another open source license.  If you want to apply a
commercial (a.k.a. proprietary) license, you must contact me first.

**However, the following files must remain under the BSD license:**

* /.pypt/commitlog
* /.pypt/ghrel
* /.pypt/localegen
* /.pypt/PYPT-UPDATE
* /.pypt/README.rst
* /.pypt/LICENSE.PyPT
* /pypt-extras/AUR_post-release.hook
* /docs/CONTRIBUTING.rst
* /CONTRIBUTING.rst
* /release

**This README file MAY NOT be relicensed.**

Copyright © 2013-2017, Chris Warrick.
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are
met:

1. Redistributions of source code must retain the above copyright
   notice, this list of conditions, and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright
   notice, this list of conditions, and the following disclaimer in the
   documentation and/or other materials provided with the distribution.

3. Neither the name of the author of this software nor the names of
   contributors to this software may be used to endorse or promote
   products derived from this software without specific prior written
   consent.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
"AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
A PARTICULAR PURPOSE ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT
OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
