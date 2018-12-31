==============
PyPT Changelog
==============
:Info: This is the changelog for PyPT.
:Author: Chris Warrick <chris@chriswarrick.com>
:Copyright: © 2013-2019, Chris Warrick.
:Date: 2019-01-01
:Version: 2.1.10

.. index:: CHANGELOG

GitHub holds releases, too
==========================

More information can be found on GitHub in the `releases section
<https://github.com/Kwpolska/python-project-template/releases>`_.

Version History
===============

2.1.10
    * Update © dates to 2019

2.1.9
    * Update © dates to 2018

2.1.8
    * README overhaul
    * ``entry_points`` created via cookiecutter question

2.1.7
    * Very minor README update (everything else unaffected)

2.1.6
    * Use Python 3 for AURvm client but ensure 2/3 compatibility

2.1.5
    * Add ``__main__.py``
    * Update some parts of the PyPT README and ``setup.py``

2.1.4
    * Fix some bugs in AUR stuff
    * Add new config variables: ``AUR_PKGNAME``, ``AUR_PKGNAME_GIT``, ``AUR_GIT_PACKAGE``
    * Update AUR stuff when running ``PYPT-UPDATE``

2.1.3
    * Create infrastructure to update AUR packages in an Arch virtual machine (``AURvm``)
    * Fix some minor typos in ``release``

2.1.2
    * Update © dates to 2017

2.1.1
    * Fix ``commitlog`` crashing due to a regex glitch (turns out ``C(.*?)``
      will match ``Chris``; changed to ``(C[A-Z]+)``)

2.1.0
    * Get rid of ``git flow`` — users should switch their main branch to
      ``master`` and delete ``develop``. This simplifies development and
      branching for most use cases.
    * Exit on errors in ``release``

2.0.7
    * Make some minor changes to CONTRIBUTING.rst
    * Use Python 3.5 in Travis

2.0.6
    * Sign releases commits and tags
    * Use new PyPI URL scheme in PKGBUILDs
    * Use correct file name for coverage exclude
    * Use repo name for gettext domain
    * Experimental support for PyQt5 in ``localegen``

2.0.5
    * Put test setup in ``setup.cfg``
    * More modern ``setup.py`` (uses ``package_data`` and ``find_packages()``, does not use
      ``requirements.txt``, removes support for ``./setup.py test``)
    * Sample hook for AUR updates
    * Fixes to tests and ``localegen``
    * Move Qt addons to ``pypt-extras/`` directory

2.0.4
    * Split out wildcard removal that may fail so that other cleanup works fine
    * Don’t remove the ``dist`` directory

2.0.3
    * Update dates to 2016

2.0.2
    * Add ``post-release.hook`` (at the very end, perfect for “Next steps” messages)

2.0.1
    * ``MAINFEST.in`` file
    * Minor bugfixes

2.0.0
    * Automation (using cookiecutter)

1.3.1

    .. code:: text

               ,---------------.
              /  /``````|``````\\
             /  /_______|_______\\________
            |]      GTI |'       |        |]
            =  .-:-.    |________|  .-:-.  =
             `  -+-  --------------  -+-  '
               '-:-'                '-:-'

1.3.0
    * Use ``argparse`` in ``commitlog`` and ``ghrel`` instead of a ``sys.argv`` hack
    * Vendor ``textwrap.indent`` in ``commitlog`` for Python 2 compatibility
    * Use ``py.test`` in the ``release`` script
    * Run tests only if they exist
    * Create and upload wheels


1.2.1
    * Use new tests in .travis.yml.


1.2.0
    * Better tests, stored in a directory and using py.test instead of unittest.


1.1.2
    * Add ``.pypt/PYPT-UPDATE`` script (copy it somewhere else and customize to your liking)


1.1.1
    * Fix ``$cmfn`` variables in ``./release``
    * Print correct release URL (``html_url`` for friendly webpage)
    * Support Transifex in locale generation (``-tx`` suffix)


1.1.0
    * Automate GitHub Releases posting. (For CMFN-based files, ``backticks`` are automatically corrected.)

1.0.9
    * Fix mismatched paths in the commit and changelog editor (cmfn) — requries update of ``.pypt/commitlog`` and ``release``
    * PEP 257 compliance

1.0.8
    * Update Sphinx ``version`` field (previously, only ``release`` was updated)

1.0.7
    * no more AUR uploads due to AURv4

1.0.6
    * Use ``twine`` instead of ``setup.py upload``
    * Fix ``aursend`` path

1.0.5
    Updating all dates to say 2015.

1.0.4
    * Rebranding: removing nickname from all *Author* lines.

1.0.3
    * changed e-mail address
    * setup.cfg
    * setuptools entry_points
    * py.test

1.0.2
    * Set the © fields to 2014.

1.0.1
    * Some small changes and fixes.

1.0.0
    * Initial release.

