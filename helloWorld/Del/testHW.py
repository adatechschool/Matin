import unittest
from HW import *

class Hello_world(unittest.TestCase):
    def test_renvoie_helloworld(self):
        self.assertEqual("Hello World!", affiche(''))

unittest.main()
