===============================================
Python Project Template.  INSERT TAGLINE HERE.™
===============================================
:Info: This is the README file for the Python Project Template.
:Author: Chris Warrick <chris@chriswarrick.com>
:Copyright: © 2013-2020, Chris Warrick.
:Date: 2020-02-23
:Version: 2.2.0

.. index: README
.. image:: https://travis-ci.org/Kwpolska/python-project-template.svg?branch=master

.. contents::

Requirements
============

Python Project Template is made possible by `Cookiecutter
<https://github.com/audreyr/cookiecutter>`_. To use the template, you will
also need:

* ``zsh`` installed (required by ``/release`` and ``/.pypt/localegen`` scripts)
* Python with ``requests`` (required by ``/.pypt/{commitlog,ghrel}``) and
  ``twine`` (required by ``/release``)
  installed, as well as ``pytest``, ``coverage`` and ``pytest-cov`` — run ``pip
  install -r requirements.txt`` to install everything
* A place to host Git repositories. GitHub is assumed, but can be changed
  (documented below)
* PGP/GPG setup (for signing release commits and tags)
* Travis CI account (if you do not want Travis CI, remove ``/.travis.yml``)

Template contents
=================

The template contains the following files to get you started:

* pre-configured Sphinx with:

  * ``CONTRIBUTING.rst`` guide (shown by GitHub when sending a pull request or an issue)
  * ``LICENSE.rst``
  * an empty ``CHANGELOG.rst``
  * ``README.rst``
  * a bare-bones ``index.rst`` page

* The exact same files in ``/``, which are fragile and **MAY NOT** be modified
  as they are replaced with copies in ``/docs`` by the ``release`` script
* ``__init__.py``, ``__main__.py`` and ``template.py`` files in the Python package directory
* A ``setup.py`` file that could be good enough for people, and that supports
  ``entry_points`` (see https://go.chriswarrick.com/entry_points).
* ``tests/`` containing some *Is My Python Sane?*-style tests (using ``pytest``)
* An automated global update script (``.pypt/PYPT-UPDATE``)
* Entry points configuration ready to be uncommented (and a matching
  ``__main__.py`` file)
* Add-ons for Qt users (in ``pypt-extras/Qt``)
* A sample hook for AUR updates (in ``pypt-extras/AUR``)
* PKGBUILDs for the Arch Linux User Repository (AUR)
* A state-of-the-art ``release`` script, the operations of which are:

  * querying the user for version number, commit message and changes
  * updating ``/docs/CHANGELOG.rst``
  * bumping the version number in all the files, changing dates where necessary
  * copying over ``/docs/README.rst``,  ``/docs/CHANGELOG.rst`` and ``/docs/CONTRIBUTING.rst`` to ``/``
  * locale generation (via the ``.pypt/localegen`` script)
  * running ``import $PROJECTLC`` and the test suite
  * uploading a source distribution and a wheel to PyPI
  * Making a Git commit and tagging the release
  * creating a GitHub Releases entry
  * updating the AUR packages (by using hooks)

Caveats and optional features
=============================

AUR support (hooks, VM automation)
----------------------------------

This template includes full support for creating and updating AUR PKGBUILDs.
Templates for stable and git packages are in the project directory.
Furthermore, there are scripts to facilitate updating AUR packages. Those are:

* /pypt-extras/AUR/hooks/post-release.hook
* /pypt-extras/AUR/AURvm/aurvm_client.py
* /pypt-extras/AUR/AURvm/aurvm_host.py
* /pypt-extras/AUR/AURvm/aurvm_heartbeat.sh

If you want to use those, copy (move) ``post-release.hook`` to
``.pypt/hooks/post-release.hook``. If you are doing releases on an Arch Linux
system, you may want to switch the default from remote to local updates.  If
you are doing releases on any other Linux/\*nix system, you also need to copy
the entire AURvm directory to ``.pypt/``, and put ``aurvm_host.py`` and
``aurvm_heartbeat.sh`` in your ``aur-pkgbuilds`` directory.

The scripts assume a very specific setup, which is as follows:

* repos for AUR packages in ``~/git/aur-pkgbuilds``
* ``UPDATE-REQUIREMENTS.py`` and ``aur.zsh`` scripts (see `Kwpolska/aur-pkgbuilds <https://github.com/Kwpolska/aur-pkgbuilds>`_)
* An Arch Linux virtual machine that is accessible using ``ssh arch`` (in ``.ssh/config``)
* Probably some others. Those were written with only one use case in mind
  (mine, unsurprisingly).

Qt support (locales, resources)
-------------------------------

If you are using PyQt or PySide, make sure to put your UI code in a
``ui`` submodule.  Copy the ``pypt-extras/Qt/resources.py`` file to that
submodule, even if you are not using resources now. Make sure to create a
``.pro`` file with your sources and locales.

If you do not want to use GitHub
--------------------------------

Search for mentions of GitHub (case-insensitively) and remove them. They
appear in some auto-generated links, for example.  The ``release`` script
assumes GitHub Releases, you can remove that part.

If you do not want to publish to the Arch User Repository
---------------------------------------------------------

Remove ``PKGBUILD``, ``PKGBUILD-git``. Set ``aur_email`` to anything.

If you do not want to use Travis CI
-----------------------------------

Remove ``.travis.yml`` and the badge in README files.

Getting started
===============

One time setup: virtualenvs and project directory
-------------------------------------------------

If you don’t know how virtualenvs work and why you should use them, read `my guide about setting up a Python development environment <https://chriswarrick.com/blog/2017/07/03/setting-up-a-python-development-environment/#installing-packages>`_.

You will need to prepare two places:

1. A place where you store your projects (git repositories). You probably have
   a folder for that already; if you don’t, use ``~/Projects`` or ``~/git``.
2. Somewhere to store virtualenvs. Using virtualenvwrapper is recommended, but
   not necessary. Don’t put your virtualenvs next to your code.

Create a virtualenv for PyPT named ``cookiecutter``. Clone the PyPT GitHub
repository to your project space. Run ``pip install -r
python-project-template/requirements.txt`` to install PyPT’s requirements to
your environment.

Starting a new project
----------------------

Activate the ``cookiecutter`` virtualenv. While in your project home, run
``cookiecutter python-project-template`` and answer the questions.
(If ``aur_email`` and ``github_username`` don’t apply, set them to anything.)

The script can optionally create an entry point to start your app from command
line. Select ``cli`` or ``gui`` if you want one. Select ``none`` otherwise. If
you don’t know why you would want one, read `my guide about entry_points <https://chriswarrick.com/blog/2014/09/15/python-apps-the-right-way-entry_points-and-scripts/>`_.

Fixing the things that cannot be automated
------------------------------------------

* You need to modify all documents that are stored in ``docs/``. Some of them
   need reST syntax fixes (title underlines). README needs real content.
* Since your first commit will **not** use the ``release`` script, you need to copy files by hand:

   1. ``/docs/README.rst`` to ``/README.rst`` and ``/README``
   2. ``/docs/CHANGELOG.rst`` to ``/CHANGELOG.rst``

* Modify ``/.pypt/config``. Verify that all settings are correct.
* Choose a license. I recommend the 3-clause BSD license, and the template
  includes a LICENSE file and licensing headers with the text of the 3-clause
  BSD license. However, most of the template is provided to you under the CC0
  license, and you are free to choose any license for your project and you can
  replace those headers, **unless** a file includes a copyright header with
  Chris Warrick’s name, or is on the list in the PyPT’s LICENSE file (also
  reproduced at the end of this README document) – those specific files are
  under the 3-clause BSD license, which requires the copyright notices to be
  left intact.
* If you’re using GitHub, generate a `GitHub Personal Access Token
  <https://github.com/settings/tokens>`_ in the ``repo`` scope and write it to
  a ``/.pypt/gh-token`` file. You may reuse tokens between different repos
  running PyPT. (This is used for automating GitHub Releases.)

Preparing code
--------------

* If you have any code, you can put it in your package already. Use
  ``template.py`` as a template for your Python files. (Remove it if you don’t
  need it, or store it somewhere else.)
* Customize ``/setup.py`` to your liking.  You should pay attention to the classifiers, requirements, and other things you desire to change.
* If you enabled entry points, edit ``__main__.py``. Remember that ``main()`` must take no
  positional/non-default arguments! If you do not want to create scripts and
  don’t want command-line interfaces, remove ``__main__.py``.
* Create a virtual environment for your project. Make sure to install
  ``requirements.txt``.

Extras
------

If you want to use AUR or Qt extras, check out the documentation (`Caveats and optional features`_).
Remove the ``pypt-extras`` directory if you don’t need anything else from it.

If you have a ``PYPT-UPDATE`` script, add your new project to the list there. If not, you may want to copy it from the repository root and set it up.

Your first commit
-----------------

Run the following commands (assumes GitHub)::

    source .pypt/config
    git init
    git remote add origin git@github.com:$GITUSER/$GITREPO
    git add .
    git commit -sm 'initial commit via @Kwpolska’s Python Project Template'
    git push -u origin master

Congratulations!

If you’re ready to make your first release
------------------------------------------

Run ``./release`` and watch magic happen. Make sure your project virtualenv is
active.

But if this is your first project, you should check if:

* GPG works on your system
* you created the virtualenv with the Python version, installed requirements
  and have activated it
* git works, and you have a GitHub access token (if desired)
* the optional features are configured properly

License
=======

The Python Project Template is provided under two licenses.

The main license of the Template, all Template-related files, and some
of the provided extras, is the 3-clause BSD license. The 3-clause BSD
license is a simple open-source license, which requires you to include
the text of the license and the copyright line (with Chris Warrick’s
name) with all distributions of the software.

The following files are under the 3-clause BSD license:

* /.pypt/commitlog
* /.pypt/ghrel
* /.pypt/localegen
* PyPT’s README (not the one installed by the template)
* /pypt-extras/AUR/hooks/post-release.hook
* /pypt-extras/AUR/AURvm/aurvm_client.py
* /pypt-extras/AUR/AURvm/aurvm_host.py
* /docs/CONTRIBUTING.rst
* /CONTRIBUTING.rst
* /release

The remaining files are themselves dual-licensed under the CC0
license. Note that some of the files contain 3-clause BSD license
headers. The 3-clause BSD license is the one I recommend for your
project, but I waive all copyright claims over these files to the
extent permitted by law, as stated in the CC0 license text. This means
that you are free to remove the license headers. You are also free to
remove those license headers and pick any other license you want, and
you are also free to use a commercial license.

3-CLAUSE BSD LICENSE
--------------------

Copyright © 2013-2020, Chris Warrick.
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


CC0 LICENSE
-----------
Creative Commons Legal Code

CC0 1.0 Universal

    CREATIVE COMMONS CORPORATION IS NOT A LAW FIRM AND DOES NOT PROVIDE
    LEGAL SERVICES. DISTRIBUTION OF THIS DOCUMENT DOES NOT CREATE AN
    ATTORNEY-CLIENT RELATIONSHIP. CREATIVE COMMONS PROVIDES THIS
    INFORMATION ON AN "AS-IS" BASIS. CREATIVE COMMONS MAKES NO WARRANTIES
    REGARDING THE USE OF THIS DOCUMENT OR THE INFORMATION OR WORKS
    PROVIDED HEREUNDER, AND DISCLAIMS LIABILITY FOR DAMAGES RESULTING FROM
    THE USE OF THIS DOCUMENT OR THE INFORMATION OR WORKS PROVIDED
    HEREUNDER.

Statement of Purpose

The laws of most jurisdictions throughout the world automatically confer
exclusive Copyright and Related Rights (defined below) upon the creator
and subsequent owner(s) (each and all, an "owner") of an original work of
authorship and/or a database (each, a "Work").

Certain owners wish to permanently relinquish those rights to a Work for
the purpose of contributing to a commons of creative, cultural and
scientific works ("Commons") that the public can reliably and without fear
of later claims of infringement build upon, modify, incorporate in other
works, reuse and redistribute as freely as possible in any form whatsoever
and for any purposes, including without limitation commercial purposes.
These owners may contribute to the Commons to promote the ideal of a free
culture and the further production of creative, cultural and scientific
works, or to gain reputation or greater distribution for their Work in
part through the use and efforts of others.

For these and/or other purposes and motivations, and without any
expectation of additional consideration or compensation, the person
associating CC0 with a Work (the "Affirmer"), to the extent that he or she
is an owner of Copyright and Related Rights in the Work, voluntarily
elects to apply CC0 to the Work and publicly distribute the Work under its
terms, with knowledge of his or her Copyright and Related Rights in the
Work and the meaning and intended legal effect of CC0 on those rights.

1. Copyright and Related Rights. A Work made available under CC0 may be
protected by copyright and related or neighboring rights ("Copyright and
Related Rights"). Copyright and Related Rights include, but are not
limited to, the following:

 i. the right to reproduce, adapt, distribute, perform, display, communicate, and translate a Work;
 ii. moral rights retained by the original author(s) and/or performer(s);
 iii. publicity and privacy rights pertaining to a person's image or likeness depicted in a Work;
 iv. rights protecting against unfair competition in regards to a Work, subject to the limitations in paragraph 4(a), below;
 v. rights protecting the extraction, dissemination, use and reuse of data in a Work;
 vi. database rights (such as those arising under Directive 96/9/EC of the European Parliament and of the Council of 11 March 1996 on the legal protection of databases, and under any national implementation thereof, including any amended or successor version of such directive); and
 vii. other similar, equivalent or corresponding rights throughout the world based on applicable law or treaty, and any national implementations thereof.

2. Waiver. To the greatest extent permitted by, but not in contravention
of, applicable law, Affirmer hereby overtly, fully, permanently,
irrevocably and unconditionally waives, abandons, and surrenders all of
Affirmer's Copyright and Related Rights and associated claims and causes
of action, whether now known or unknown (including existing as well as
future claims and causes of action), in the Work (i) in all territories
worldwide, (ii) for the maximum duration provided by applicable law or
treaty (including future time extensions), (iii) in any current or future
medium and for any number of copies, and (iv) for any purpose whatsoever,
including without limitation commercial, advertising or promotional
purposes (the "Waiver"). Affirmer makes the Waiver for the benefit of each
member of the public at large and to the detriment of Affirmer's heirs and
successors, fully intending that such Waiver shall not be subject to
revocation, rescission, cancellation, termination, or any other legal or
equitable action to disrupt the quiet enjoyment of the Work by the public
as contemplated by Affirmer's express Statement of Purpose.

3. Public License Fallback. Should any part of the Waiver for any reason
be judged legally invalid or ineffective under applicable law, then the
Waiver shall be preserved to the maximum extent permitted taking into
account Affirmer's express Statement of Purpose. In addition, to the
extent the Waiver is so judged Affirmer hereby grants to each affected
person a royalty-free, non transferable, non sublicensable, non exclusive,
irrevocable and unconditional license to exercise Affirmer's Copyright and
Related Rights in the Work (i) in all territories worldwide, (ii) for the
maximum duration provided by applicable law or treaty (including future
time extensions), (iii) in any current or future medium and for any number
of copies, and (iv) for any purpose whatsoever, including without
limitation commercial, advertising or promotional purposes (the
"License"). The License shall be deemed effective as of the date CC0 was
applied by Affirmer to the Work. Should any part of the License for any
reason be judged legally invalid or ineffective under applicable law, such
partial invalidity or ineffectiveness shall not invalidate the remainder
of the License, and in such case Affirmer hereby affirms that he or she
will not (i) exercise any of his or her remaining Copyright and Related
Rights in the Work or (ii) assert any associated claims and causes of
action with respect to the Work, in either case contrary to Affirmer's
express Statement of Purpose.

4. Limitations and Disclaimers.

 a. No trademark or patent rights held by Affirmer are waived, abandoned,
    surrendered, licensed or otherwise affected by this document.
 b. Affirmer offers the Work as-is and makes no representations or
    warranties of any kind concerning the Work, express, implied,
    statutory or otherwise, including without limitation warranties of
    title, merchantability, fitness for a particular purpose, non
    infringement, or the absence of latent or other defects, accuracy, or
    the present or absence of errors, whether or not discoverable, all to
    the greatest extent permissible under applicable law.
 c. Affirmer disclaims responsibility for clearing rights of other persons
    that may apply to the Work or any use thereof, including without
    limitation any person's Copyright and Related Rights in the Work.
    Further, Affirmer disclaims responsibility for obtaining any necessary
    consents, permissions or other rights required for any use of the
    Work.
 d. Affirmer understands and acknowledges that Creative Commons is not a
    party to this document and has no duty or obligation with respect to
    this CC0 or use of the Work.
