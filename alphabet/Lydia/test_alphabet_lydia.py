import unittest
from alphabet_lydia import *

class afficher_alphabet(unittest.TestCase):
    def test_alphabet(self):
        self.assertEqual("abcdefghijklmnopqrstuvwxyz", affiche_alphabet())

unittest.main()
