#!/usr/bin/python
# -*- encoding: utf-8 -*-
# TEMPLATE v0.1.0
# INSERT TAGLINE HERE.
# Copyright © 2015, Chris Warrick.
# See /LICENSE for licensing information.
# This file is originally a part of the Python Project Template.

"""
Adapt Qt resources to Python version.

:Copyright: © 2015, Chris Warrick.
:License: BSD (see /LICENSE).
"""
import sys

if sys.version_info[0] == 2:
    import tEmplate.ui.resources2  # NOQA
elif sys.version_info[0] == 3:
    import tEmplate.ui.resources3  # NOQA
else:
    print('FATAL: python version does not match `2` nor `3`')
    sys.exit(0)
