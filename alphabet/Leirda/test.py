import unittest
from alpha import *

class alpha(unittest.TestCase):
    def test_alpha(self):
        self.assertEqual(alpha_low(), "abcdefghijklmnopqrstuvwxyz")

unittest.main()
