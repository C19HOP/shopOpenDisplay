import unittest
from app import isTheShopCurrentlyOpen
#from app import app

class Test(unittest.TestCase):
    def test(self):
      self.assertTrue(isTheShopCurrentlyOpen('09:00:00','17:00:00','10:00:00') =='open')


