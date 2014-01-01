#!/usr/bin/python
# -*- encoding: utf-8 -*-
# TEMPLATE v0.1.0
# INSERT TAGLINE HERE.
# Copyright © 2014, Kwpolska.
# See /LICENSE for licensing information.
# This file is originally a part of the Python Project Template.

"""
    tEmplate.ui.resources
    ~~~~~~~~~~~~~~~~~~~~~

    Adapts Qt resources to Python version.

    :Copyright: © 2014, Kwpolska.
    :License: BSD (see /LICENSE).
"""
import sys

if sys.version_info[0] == 2:
    import tEmplate.ui.resources2
elif sys.version_info[0] == 3:
    import tEmplate.ui.resources3
else:
    print('FATAL: python version does not match `2` nor `3`')
    sys.exit(0)
