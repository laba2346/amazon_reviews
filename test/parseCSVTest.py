import unittest
import sys
import csv
import os
sys.path.append('..')

from main import parseCSV
from word import Word

class TestParseCSV(unittest.TestCase):
    def test_first_row(self):
        os.chdir("..")
        expRow = []
        #Get current first row, then append to it the expected columns
        with open("example2.csv", 'r') as csvInput:
            reader = csv.reader(csvInput, delimiter=",", quotechar='"')
            expRow = next(reader)
            csvInput.seek(0)
        expRow.append("NLET")
        expRow.append("NPHON")
        expRow.append("NSYL")
        expRow.append("KFFREQ")
        expRow.append("KFCATS")
        expRow.append("KFSAMPS")
        expRow.append("TLFREQ")
        expRow.append("BFREQ")
        expRow.append("FAM")
        expRow.append("CONC")
        expRow.append("IMAG")
        expRow.append("MEANC")
        expRow.append("MEANP")
        expRow.append("AOA")

        #Parse CSV, and check the first row to verify that it's correct
        parseCSV("example2.csv")
        with open("out.csv", 'r') as csvOutput:
            reader = csv.reader(csvOutput, delimiter=',', quotechar='"')
            gotRow = next(reader)
            self.assertEqual(expRow, gotRow)

if __name__ == '__main__':
    unittest.main()
