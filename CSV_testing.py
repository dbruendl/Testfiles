__author__ = 'Meins'

import unittest
from CSV.csv_rw import *


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.testcsv = csv_rw("ergebnisse.csv")
        pass

    def testread(self):
        self.testcsv.readf("ergebnisse.csv")

    def testwrite(self):
        self.testcsv.writef("test.csv")

    def testread2(self):
        self.testcsv.readf("test.csv")

    def testread3(self):
        self.testcsv.readf("test.txt")



if __name__ == '__main__':
    unittest.main()
