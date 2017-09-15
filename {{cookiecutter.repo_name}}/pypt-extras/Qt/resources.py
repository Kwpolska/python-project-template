# -*- encoding: utf-8 -*-
# {{ cookiecutter.project_name }} v{{ cookiecutter.version }}
# {{ cookiecutter.project_short_description }}
# Copyright © {{ cookiecutter.year }}, {{ cookiecutter.full_name }}.
# See /LICENSE for licensing information.
# This file was adapted from Chris Warrick’s Python Project Template.

"""
Adapt Qt resources to Python version.

:Copyright: © {{ cookiecutter.year }}, {{ cookiecutter.full_name }}.
:License: BSD (see /LICENSE).
"""

__all__ = ()

import sys

if sys.version_info[0] == 2:
    import {{ cookiecutter.repo_name }}.ui.resources2  # NOQA
elif sys.version_info[0] == 3:
    import {{ cookiecutter.repo_name }}.ui.resources3  # NOQA
else:
    print('FATAL: python version does not match `2` nor `3`')
    sys.exit(0)
