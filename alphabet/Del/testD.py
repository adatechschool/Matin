import unittest
from fonctionD import *

class alphabet(unittest.TestCase):
    def test_revoie_minus(self):
        self.assertEqueal('', minus("abcdefghijklmnopqrstuvwxyz"))
#    def test_revoie_maj(self):
#        self.assertEqual('', maj("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

unittest.main()
