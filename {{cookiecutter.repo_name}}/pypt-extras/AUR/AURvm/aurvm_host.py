#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# AURvm host script
# Usage: base64-encoded JSON on stdin
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
import os
import subprocess
import sys

BASEDIR = os.path.expanduser('~/git/aur-pkgbuilds')


def commitaur(msg):
    with open('.SRCINFO', 'wb') as fh:
        fh.write(subprocess.check_output(['makepkg', '--printsrcinfo']))
    subprocess.check_call(['git', 'add', '.'])
    subprocess.check_call(['git', 'commit', '-asm', msg])
    subprocess.check_call(['git', 'push', '-u', 'origin', 'master'])


data = base64.b64decode(sys.stdin.read().encode('utf-8'))
data = json.loads(data.decode('utf-8'))
if data['_api'] != '2':
    print("API version does not match")

msg = data['project'] + ' v' + data['version']
sys.stderr.write("[host] Updating AUR packages...\n")
sys.stderr.flush()

os.chdir(BASEDIR)
os.chdir(data['aur_pkgname'])
with io.open('PKGBUILD', 'w', encoding='utf-8') as fh:
    fh.write(data['pkgbuild'])
commitaur(msg)
os.chdir(BASEDIR)

if data['use_git']:
    os.chdir(data['aur_pkgname_git'])
    subprocess.check_call(["sed", "s/pkgver=.*/pkgver=" + data['gitver'] + "/", "PKGBUILD", "-i"])
    commitaur(msg)
    os.chdir(BASEDIR)

subprocess.check_call(['./UPDATE-REQUIREMENTS.py'])
subprocess.check_call(['git', 'commit', '-asm', msg])
subprocess.check_call(['git', 'push'])
sys.stderr.write("[host] Done!\n")
sys.stderr.flush()
