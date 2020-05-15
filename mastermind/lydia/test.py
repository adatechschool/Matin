#!/usr/bin/env python

import unittest
from codemaker import *


class Decodeur(unittest.TestCase):
    def test_renvoie_bleu_rouge(self):
        self.assertEqual(decodeur("0,1"), "0,1")

unittest.main()
