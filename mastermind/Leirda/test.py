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
        self.assertEqual(hint([Color.red, Color.yellow], [Color.red, Color.pink, Color.yellow]), [1, 1])

class pad_none_to_list(unittest.TestCase):
    def test_list_pad(self):
        self.assertEqual(list_pad([0, 1, 1], 3), [0, 1, 1, None, None, None])
    def test_list_pad_negative(self):
        self.assertEqual(list_pad(["hello", ", world!"], -3), ["hello", ", world!"])

unittest.main()
