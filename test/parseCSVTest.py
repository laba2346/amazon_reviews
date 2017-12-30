import unittest
import sys
import csv
import os
sys.path.append('..')

from main import parseCSV
from word import Word

class TestParseCSV(unittest.TestCase):
    def test_first_row(self):
        os.chdir("/Users/landon/Dropbox/Amazon project/")
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

    #Once a review is scored, its data is written to a CSV. This tests the
    #output of a single review.
    def test_second_row(self):
        os.chdir("/Users/landon/Dropbox/Amazon project/")
        expRow = []
        #Get the current row for the first review before we append to it
        with open("example2.csv", 'r') as csvInput:
            reader = csv.reader(csvInput, delimiter=",", quotechar='"')
            row0 = next(reader)
            expRow = next(reader)
            csvInput.seek(0)
        expRow.append("63")
        expRow.append("48")
        expRow.append("17")
        expRow.append("72161")
        expRow.append("145")
        expRow.append("1569")
        expRow.append("254340")
        expRow.append("7531")
        expRow.append("5021")
        expRow.append("3903")
        expRow.append("4088")
        expRow.append("3534")
        expRow.append("688")
        expRow.append("614")

        #parse the csv and produce the "got" output
        parseCSV("example2.csv")

        with open("out.csv", 'r') as csvOutput:
            reader = csv.reader(csvOutput, delimiter=',', quotechar='"')
            row0 = next(reader)
            gotRow = next(reader)
            self.assertEqual(expRow, gotRow)

if __name__ == '__main__':
    unittest.main()
