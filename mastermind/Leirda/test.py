#!/usr/bin/env python3
import unittest
from mastermind import *


class give_mastermind_code_hint(unittest.TestCase):
    def test_no_clue(self):
        self.assertEqual(hint([Color.blue], [Color.red]), [0, 0])
    def test_1_well_placed(self):
        self.assertEqual(hint([Color.blue], [Color.blue]), [1, 0])
    def test_1_misplaced(self):
        self.assertEqual(hint([Color.red, Color.yellow], [Color.blue, Color.red]), [0, 1])

    def test_1_well_placed_1_misplaced(self):
        self.assertEqual(hint([Color.red, Color.yellow, Color.green], [Color.red, Color.pink, Color.yellow]), [1, 1])

unittest.main()
