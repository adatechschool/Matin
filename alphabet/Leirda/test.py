import unittest
from alpha import *

class alpha(unittest.TestCase):
    def test_alpha_default(self):
        self.assertEqual(alpha_low(), "abcdefghijklmnopqrstuvwxyz")

    def test_alpha_a_to_z(self):
        self.assertEqual(alpha_low("a-z"), "abcdefghijklmnopqrstuvwxyz")

    def test_alpha_d_to_y(self):
        self.assertEqual(alpha_low("d-y"), "defghijklmnopqrstuvwxy")

unittest.main()
