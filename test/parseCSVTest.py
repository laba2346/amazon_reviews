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
        expRow.append("Word count")
        expRow.append("numNLET")
        expRow.append("sumNLET")
        expRow.append("avgNLET")

        expRow.append("numNPHON")
        expRow.append("sumNPHON")
        expRow.append("avgNPHON")

        expRow.append("numNSYL")
        expRow.append("sumNSYL")
        expRow.append("avgNSYL")

        expRow.append("numKFFREQ")
        expRow.append("sumKFFREQ")
        expRow.append("avgKFFREQ")

        expRow.append("numKFCATS")
        expRow.append("sumKFCATS")
        expRow.append("avgKFCATS")

        expRow.append("numKFSAMPS")
        expRow.append("sumKFSAMPS")
        expRow.append("avgKFSAMPS")

        expRow.append("numTLFREQ")
        expRow.append("sumTLFREQ")
        expRow.append("avgTLFREQ")

        expRow.append("numBFREQ")
        expRow.append("sumBFREQ")
        expRow.append("avgBFREQ")

        expRow.append("numFAM")
        expRow.append("sumFAM")
        expRow.append("avgFAM")

        expRow.append("numCONC")
        expRow.append("sumCONC")
        expRow.append("avgCONC")

        expRow.append("numIMAG")
        expRow.append("sumIMAG")
        expRow.append("avgIMAG")

        expRow.append("numMEANC")
        expRow.append("sumMEANC")
        expRow.append("avgMEANC")

        expRow.append("numMEANP")
        expRow.append("sumMEANP")
        expRow.append("avgMEANP")

        expRow.append("numAOA")
        expRow.append("sumAOA")
        expRow.append("avgAOA")

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
        expRow.append("16")
        expRow.append("16")
        expRow.append("77")
        expRow.append("4.812")
        expRow.append("13")
        expRow.append("49")
        expRow.append("3.769")
        expRow.append("13")
        expRow.append("17")
        expRow.append("1.308")
        expRow.append("13")
        expRow.append("2589")
        expRow.append("199.154")
        expRow.append("13")
        expRow.append("145")
        expRow.append("11.154")
        expRow.append("13")
        expRow.append("1279")
        expRow.append("98.385")
        expRow.append("11")
        expRow.append("27083")
        expRow.append("2462.091")
        expRow.append("14")
        expRow.append("949")
        expRow.append("67.786")
        expRow.append("9")
        expRow.append("5003")
        expRow.append("555.889")
        expRow.append("9")
        expRow.append("4042")
        expRow.append("449.111")
        expRow.append("9")
        expRow.append("4274")
        expRow.append("474.889")
        expRow.append("8")
        expRow.append("3754")
        expRow.append("469.25")
        expRow.append("1")
        expRow.append("688")
        expRow.append("688.0")
        expRow.append("3")
        expRow.append("839")
        expRow.append("279.667")
        
        #parse the csv and produce the "got" output
        parseCSV("example2.csv")

        with open("out.csv", 'r') as csvOutput:
            reader = csv.reader(csvOutput, delimiter=',', quotechar='"')
            row0 = next(reader)
            gotRow = next(reader)
            self.assertEqual(expRow, gotRow)

if __name__ == '__main__':
    unittest.main()
