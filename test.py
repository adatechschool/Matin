import unittest
from fonction import *

class alphabet(unittest.TestCase):
    def revoie_alphabet(self):
        self.assertEqueal('',afficheAlphabet("abcdefghijklmnopqrstuvwxyz"))

unittest.main()
