__author__ = 'Meins'

import unittest
from CSV.csv_rw import *


class MyTestCase(unittest.TestCase):

    def testread(self):
        csv_rw.readf(self,"ergebnisse.csv")

    def testwrite(self):
        csv_rw.writef(self,"test.csv")

    def testread2(self):
        csv_rw.readf(self,"test.csv")

    def testread3(self):
        csv_rw.readf(self,"test.txt")



if __name__ == '__main__':
    unittest.main()
