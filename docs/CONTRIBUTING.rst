==============================
Appendix A. Contribution rules
==============================
:Author: Chris “Kwpolska” Warrick <kwpolska@kwpolska.tk>
:Copyright: © 2013, Kwpolska.
:License: BSD (see /LICENSE or :doc:`Appendix B <LICENSE>`.)
:Date: 2013-01-20
:Version: 0.1.0

.. index:: contributing

Do you want to contribute to this project?  Great!  I’d love to see some help,
but you must comply with some rules.

The key words “MUST”, “MUST NOT”, “REQUIRED”, “SHALL”, “SHALL
NOT”, “SHOULD”, “SHOULD NOT”, “RECOMMENDED”,  “MAY”, and
“OPTIONAL” in this document are to be interpreted as described in
RFC 2119.

---------------
Issue reporting
---------------

.. index:: issues

GitHub Issues are the recommended way to report an issue.  If you do not have an
account there, get one or mail me.

When pasting console sessions, you must paste them fully,
*prompt-to-prompt*, to see all the messages and your input.
Trim only stuff that you are 1000% sure that is not related
to the project in question.

--------------------------------------------
General preparations, rules and pull process
--------------------------------------------

Prepare
=======

A GitHub account is recommended.  Patches by mail are accepted, but working
with you through there is a better way.

Fork the repo first.  Non-GitHub people, ``git clone``.

.. _Rules:

Rules
=====

1. Commits must have short, informative and logical messages.  Signoffs and
   long messages are recommended.  “fixes #xxx” is required if an issue
   exists.
2. The following fancy Unicode characters should be used when
   needed: ``— “ ” ‘ ’``
3. The ellipsis (``…``) character must not be used in program output for
   humans, but may be used elsewhere.
4. I’m a Grammar Nazi.

Request a Pull
==============

Done?  Go hit the **Pull Request** button over on GitHub!  And if you don’t
use GitHub, ``git format-patch``.  Other formats are not accepted.

Your commit should be pulled up in a (longer) while.  If I like it.  Because
some commits may be bad.  So, do your best not to do those bad commits.

---------------------------------------
Details for specific contribution types
---------------------------------------

Code (Python)
=============

1. PEP 8.  ``pip install pep8`` is recommended.
2. ``./tests.py``.
3. Localize all the strings (``_('string')``)
4. Strings must be quoted using ``'str'``.  Multi-line strings, ``"""str"""``.
   Use the latter only if needed.  Otherwise, do:

.. code-block:: python
   :linenos:

   string = ('A very, very, very long string '
             'that’s broken up into multiple lines.')

   string = _('A very, very, very log string '
              'that’s broken up into multiple lines '
              'and that is localized through gettext.'))

5. ``str.format``.  Braces should be empty or contain a name that is later
   passed on to the function.  The format function should be inserted *after*
   the parenthesis for string localization.  For example:

.. code-block:: python
   :linenos:

   string = _('{} is awesome').format('PKGBUILDer')
   string = _('{sth} is awesome').format(sth='PKGBUILDer')

6. Documentation is important.  Please take care of it.

Code (non-Python)
=================

Rejected.

Non-code contributions
======================

Those are accepted.  No specific rules exist.  And don’t remove any files
without my permission (``docs/*.8.gz`` in particular).

Localization
============

.. index:: locale

1. Run ``mkdir -p locale/[CODE]/LC_MESSAGES`` in your terminal, replacing
   ``[CODE]`` by your language code, as in /usr/share/locale.
2. Copy the ``/messages.pot`` file to
   ``locale/[CODE]/LC_MESSAGES/[PROJECT].po`` (replace ``[PROJECT]`` with the
   project name, all-lowercase)
3. Do your work.  The comments will inform you where this string is, and the
   ones starting with 'TRANSLATORS:' are for you to read and make use of.
   Other comments come from my code and you should not care about them.  And
   if it is directed for translators, let me know.  The Poedit_ app may be
   of help.  Please take care of the headers at the top of the file (with a
   text editor, do not use Poedit for that!)  and modify them.  The
   Last-Translator, Language-Team and Language are important, the others are
   auto-generated anyways.  The general :ref:`Rules` apply, please take care
   of it!
4. Commit (``-s/--signoff`` is required here).
5. Your translation will be added in the next release, or, if a release isn’t
   planned in the near future, a new release will be made.  Your addition will
   be appreciated.  Note that I cannot translate new strings, and, as a result,
   I might ask you for additions in the future.

.. _Poedit: http://www.poedit.net/
