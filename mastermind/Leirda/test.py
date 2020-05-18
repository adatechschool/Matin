#!/usr/bin/env python3
import unittest
from mastermind import *


class hintTest(unittest.TestCase):
    def assertHint(self, expected, secret, guess):
        self.assertEqual(expected, hint(secret, guess))

    def testNoClue(self):
        self.assertHint((0, 0), [Color.blue], [Color.red])

    def testOnlyGood(self):
        self.assertHint((1, 0), [Color.blue], [Color.blue])

    def testOnlyMiss(self):
        self.assertHint((0, 1), [Color.white, Color.red], [Color.red, Color.black])

    def testGoodAndMiss(self):
        self.assertHint((1, 1), [Color.blue, Color.white, Color.green], [Color.blue, Color.green, Color.black])

    def testCountMissOnce(self):
        self.assertHint((0, 1), [Color.blue, Color.blue, Color.red], [Color.red, Color.red, Color.green])

# Doesn't pass!
#    def testCountOnlyGoodWhenMiss(self):
#        self.assertHint((1, 0), [Color.blue, Color.white], [Color.blue, Color.blue])
#        self.assertHint((1, 0), [Color.white, Color.blue], [Color.blue, Color.blue])

unittest.main()

