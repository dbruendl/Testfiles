__author__ = 'Meins'

import unittest
from csv_rw import *

class MyTestCase(unittest.TestCase):

    def testread(self):
        self.b = readf("ergebnisse.csv")
        pass





if __name__ == '__main__':
    unittest.main()
