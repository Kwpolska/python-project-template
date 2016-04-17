#!/usr/bin/python
# -*- encoding: utf-8 -*-
# TODO: replace PROJECTNAME with the correct name
# TODO: fix header and docstring
# TODO: remove exception
# HEADER LINE 1
# HEADER LINE 2
# HEADER LINE 3
# See /LICENSE for licensing information.
# This file is originally a part of the Python Project Template.

"""Adapt Qt resources to Python version."""
import sys

raise Exception("Please edit resources.py (see TODO tags) and remove me.")

if sys.version_info[0] == 2:
    import PROJECTNAME.ui.resources2  # NOQA
elif sys.version_info[0] == 3:
    import PROJECTNAME.ui.resources3  # NOQA
else:
    print('FATAL: python version does not match `2` nor `3`')
    sys.exit(0)
