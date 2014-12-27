#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# TEMPLATE test suite
# Copyright © 2014, Chris Warrick.
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

import tEmplate
import tEmplate.template
import unittest


class TestTEMPLATE(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_false(self):
        self.assertFalse(False)

    def test_trueexpr(self):
        self.assertTrue(1 == 1)

    def test_falseexpr(self):
        self.assertFalse(1 == 2)

    def test_maths(self):
        self.assertEqual(2 + 2, 4)
        self.assertEqual(2 - 2, 0)
        self.assertEqual(2 * 2, 4)
        self.assertEqual(2 / 2, 1)
        self.assertEqual(3 % 2, 1)

    def test_bitwise(self):
        self.assertEqual(0b11 ^ 0b10, 0b01)
        self.assertEqual(0b100 | 0b010, 0b110)
        self.assertEqual(0b101 & 0b011, 0b001)
        self.assertEqual(0b10 << 2, 0b1000)
        self.assertEqual(0b1111 >> 2, 0b11)

if __name__ == '__main__':
    unittest.main()
