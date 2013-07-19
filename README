===============================================
Python Project Template.  INSERT TAGLINE HERE.™
===============================================
:Info: This is the README file for the Python Project Template.
:Author: Kwpolska <kwpolska@kwpolska.tk>
:Date: 2013-01-20
:Version: 0.1.0

.. index: README
.. image:: https://travis-ci.org/Kwpolska/python-project-template.png?branch=master

USING THE TEMPLATE
------------------

Requirements
============

* ``zsh`` installed (``/release`` and ``/.pypt/localegen`` scripts)
* Python with ``requests`` installed (``/.pypt/{commitlog,aursend}``)
* `git-flow extensions by nvie <https://github.com/nvie/gitflow>`_ (you need
  to manually alter the ``/release`` script, and that is much harder than
  installing the extensions)
* A git repository.  The PyPT is ready to go if you use GitHub.  If you do not
  want GitHub, edit the ``/PKGBUILD{,-2}{,-git}`` files and any other places
  where GitHub is mentioned, including this document which you should edit
  mentally.

Recommended possesions
======================

* Travis CI account (if you do not want Travis CI, remove ``/.travis.yml``)
* AUR account (if you do not want AUR uploads, remove the
  ``/PKGBUILD{,-2}{,-git}`` files and modify the ``/.pypt/config`` file)

Contents
========

The template contains the following files to get you started:

* pre-configured Sphinx with:

  * ``CONTRIBUTING.rst`` guide (used by GitHub when sending a pull request or an issue)
  * ``LICENSE.rst``
  * an empty ``CHANGELOG.rst``
  * this (worthless for most people) ``README.rst`` and a bare-bones ``index.rst`` page

* The exact same files in ``/``, which are fragile and **MAY NOT** be modified
  as they are replaced with copies in ``/docs`` by the ``release``
  script
* ``__init__.py`` and ``template.py`` files in the Python package directory
* A good-enough ``setup.py`` file
* ``tests.py`` containing some *Is My Python Sane?*-style tests
* A sample ``/usr/bin/`` script
* Addons for Qt users
* PKGBUILDs for the Arch Linux User Repository (AUR)
* A state-of-the-art ``release`` script, the operations of which are:

  * querying the current branch for version number
  * updating ``/docs/CHANGELOG.rst``
  * bumping the version number in all the files, changing dates where necessary
  * copying over ``/docs/README.rst``,  ``/docs/CHANGELOG.rst`` and ``/docs/CONTRIBUTING.rst`` to ``/``
  * locale generation (via the ``.pypt/localegen`` script)
  * running ``import $project`` and the testsuite
  * creating and uploading AUR packages
  * commiting into git, finishing the ``git flow`` release


Getting up to speed in 15 easy steps
====================================

1. Create the repository for the project on GitHub and enable it on Travis CI.
2. Manually change ``Kwpolska`` to your GitHub name in the following files:

   1. ``/docs/README.rst``, line 10
   2. ``/docs/CHANGELOG.rst``, line 10
   3. ``/setup.py``, line 14
   4. ``/PKGBUILD{,-2}{,-git}``, in ``url`` and ``source`` (git only)

3. Manually change the ``Maintainer`` line in ``/PKGBUILD{,-2}{,-git}``.
4. Replace the following patterns (eg. with sed), in all files, **excluding
   dotfiles**:

   1. ``TEMPLATE`` with the full name of the project
   2. ``tEmplate`` with a “light” name of the project [a-z0-9\_\\-], which will
      be used in the PyPI, AUR, and a few other places.  You can use capital
      letters if you feel like it, but it is discouraged and was not tested.
   3. ``python-project-template`` with the GitHub repo name
   4. ``INSERT TAGLINE HERE.`` with a tagline of your choice
   5. ``kwpolska@.*`` with your e-mail address
   6. ``Kwpolska`` with your name (affects mostly copyright notices)

   Not excluding dotfiles results in changing BSD-licensed files of the PyPT,
   doing so is not allowed.

   Also, if ``len(computer_friendly_name) != len('tEmplate')``, you may want to
   change the amount of tildes in docstrings of Python files.

4. Rename ``/tEmplate`` to the name used in 4.2.
5. Modify ``/docs/README.rst`` to reflect your project and not the Template
   (and make a copy if you are reading it locally from those files)
6. Copy: (when using the included ``release`` script, it happens automatically)

   1. ``/docs/README.rst`` to ``/README.rst`` and ``/README``
   2. ``/docs/CHANGELOG.rst`` to ``/CHANGELOG.rst``

7. Modify ``/.pypt/config``
8. Modify ``/bin/tEmplate`` and rename it OR remove the directory
9. Customize ``/setup.py`` to your liking.  You should pay attention to the
   classifiers and the commented parts.
10. Customize requirements.txt.
11. If you are using PyQt4 or PySide, make sure to put your UI code in a ``ui``
    submodule.  Copy over the ``/QT-ADDONS/resources.py`` file to that
    submodule, even if you are not using resources now.
12. Remove the ``/QT-ADDONS/`` directory.
13. If you are using Qt, make sure to create a ``.pro`` file with your sources
    and locales.
14. Read the COPYRIGHT section below (or ``LICENSE.PyPT``) and remove
    ``/LICENSE.PyPT`` and ``/README.PyPT``.  If you believe the BSD license presented by the
    ``/LICENSE`` file is not the license you want, here is a list of files you
    should modify:

    1. ``/tests.py``
    2. Everything in the Python package directory (twice in many cases)
    3. Everything in ``/docs``
    4. ``/LICENSE``, which is **not** equivalent to ``/docs/LICENSE.rst``

    PS. GNU GPL is not a good idea.  You can use it, but the world would be
    much happier if you did not.

15. Remove ``/.git``, and run the following commands, replacing stuff with ``$``
    in front::

        git init
        git remote add origin git@github.com:$GITUSERNAME/$GITREPO
        git flow init #(change version tag prefix to `v`)
        git add *
        git checkout develop
        git commit -sm 'initial commit via Kwpolska’s Python Project Template'
        git checkout master
        git merge --ff-only develop
        git push -u origin master develop

Note that the above is likely to be replaced with an automated script at some
point.

COPYRIGHT
---------

Python Project Template is licensed under a BSD-like license.  You are free to
relicense your code to another open source license.  If you want to apply a
commercial (a.k.a. proprietary) license, you must contact me first.

**However, the following files must remain under the BSD license:**

* /.pypt/aursend
* /.pypt/commitlog
* /.pypt/localegen
* /.pypt/README.PyPT
* /.pypt/LICENSE.PyPT
* /release

**This README file MAY NOT be relicensed.**

Copyright © 2013, Kwpolska.
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
