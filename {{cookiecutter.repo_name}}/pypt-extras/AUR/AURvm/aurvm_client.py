#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# AURvm client script
# Usage: ./aurvm_client.py $PROJECT $AUR_PKGNAME $AUR_PKGNAME_GIT $version use_git[true|false]
# Part of the Python Project Template.
# Copyright © 2013-2018, Chris Warrick.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions, and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions, and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
#
# 3. Neither the name of the author of this software nor the names of
#    contributors to this software may be used to endorse or promote
#    products derived from this software without specific prior written
#    consent.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import base64
import io
import json
import subprocess
import sys

try:
    _, project, aur_pkgname, aur_pkgname_git, version, use_git = sys.argv
except ValueError:
    sys.stderr.write("Usage: ./aurvm_client.py $PROJECT $AUR_PKGANME $AUR_PKGNAME_GIT $version use_git[true|false]\n")
    sys.exit(1)

use_git = True if use_git == 'true' else False
if use_git:
    gitver = subprocess.check_output(r"git describe --long | sed -E 's/([^-]*-g)/r\1/;s/-/./g;s/^v//g'", shell=True)
    gitver = gitver.decode('utf-8').strip()
else:
    gitver = None

with io.open('PKGBUILD', 'r', encoding='utf-8') as fh:
    pkgbuild = fh.read()

data = json.dumps({
    'project': project,
    'aur_pkgname': aur_pkgname,
    'aur_pkgname_git': aur_pkgname_git,
    'version': version,
    'use_git': use_git,
    'gitver': gitver,
    'pkgbuild': pkgbuild,
    '_api': '2'
}, ensure_ascii=True, sort_keys=True).encode('utf-8')

print(base64.b64encode(data).decode('utf-8'))
