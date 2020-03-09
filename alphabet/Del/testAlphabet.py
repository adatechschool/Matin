import unittest
from alphabet import *

class alphabet(unittest.TestCase):
    def test_revoie_minus(self):
        self.assertEqual("abcdefghijklmnopqrstuvwxyz", minus())
    def test_revoie_maj(self):
        self.assertEqual("ABCDEFGHIJKLMNOPQRSTUVWXYZ", maj())

unittest.main()
