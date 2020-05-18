#!/usr/bin/env python3
import unittest
from mastermind import *


class hintTest(unittest.TestCase):
    def assertHint(self, expected, secret, guess):
        self.assertEqual(expected, hint(secret, guess))

    def test_no_clue(self):
        self.assertHint((0, 0), [Color.blue], [Color.red])

    def test_only_good(self):
        self.assertHint((1, 0), [Color.blue], [Color.blue])

    def test_only_miss(self):
        self.assertHint((0, 1), [Color.white, Color.red], [Color.red, Color.black])

    def test_mix_good_miss(self):
        self.assertHint((1, 1), [Color.blue, Color.white, Color.green], [Color.blue, Color.green, Color.black])

    def test_count_miss_once(self):
        self.assertHint((0, 1), [Color.blue, Color.blue, Color.red], [Color.red, Color.red, Color.green])

unittest.main()
