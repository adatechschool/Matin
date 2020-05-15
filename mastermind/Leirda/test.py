import unittest
from mastermind import *

class give_hint(unittest.TestCase):
    def test_no_clue(self):
        self.assertEqual(hint([Color.blue], [Color.red]), [0, 0])
    def test_1_well_placed(self):
        self.assertEqual(hint([Color.blue], [Color.blue]), [1, 0])

unittest.main()
