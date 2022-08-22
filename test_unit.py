import unittest
from app import isTheCurrentlyShopOpen
#from app import app

class Test(unittest.TestCase):
    def test(self):
      self.assertEqual(isTheCurrentlyShopOpen('09:00:00','17:00:00','10:00:00'), msg='open')
     # self.assertTrue(make_dough('flour','water') == 'dough')
     # self.assertTrue(make_dough('blah','blah') == 'not dough')

