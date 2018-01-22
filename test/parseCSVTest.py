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
        expRow.append("73")
        expRow.append("4.562")
        expRow.append("13")
        expRow.append("47")
        expRow.append("3.615")
        expRow.append("14")
        expRow.append("17")
        expRow.append("1.214")
        expRow.append("14")
        expRow.append("3215")
        expRow.append("229.643")
        expRow.append("14")
        expRow.append("162")
        expRow.append("11.571")
        expRow.append("14")
        expRow.append("1560")
        expRow.append("111.429")
        expRow.append("13")
        expRow.append("28502")
        expRow.append("2192.462")
        expRow.append("14")
        expRow.append("956")
        expRow.append("68.286")
        expRow.append("11")
        expRow.append("6143")
        expRow.append("558.455")
        expRow.append("11")
        expRow.append("4691")
        expRow.append("426.455")
        expRow.append("11")
        expRow.append("4952")
        expRow.append("450.182")
        expRow.append("10")
        expRow.append("4555")
        expRow.append("455.5")
        expRow.append("1")
        expRow.append("688")
        expRow.append("688.0")
        expRow.append("3")
        expRow.append("883")
        expRow.append("294.333")

        #parse the csv and produce the "got" output
        parseCSV("example2.csv")

        with open("out.csv", 'r') as csvOutput:
            reader = csv.reader(csvOutput, delimiter=',', quotechar='"')
            row0 = next(reader)
            gotRow = next(reader)
            self.assertEqual(expRow, gotRow)

    def test_three_rows(self):
        os.chdir("/Users/landon/Dropbox/Amazon project/")
        expRow1 = []
        expRow2 = []
        #Get the current row for the first review before we append to it
        with open("example2.csv", 'r') as csvInput:
            reader = csv.reader(csvInput, delimiter=",", quotechar='"')
            row0 = next(reader)
            expRow1 = next(reader)
            expRow2 = next(reader)
            csvInput.seek(0)
        exp1 = [16, 16, 73, 4.562, 13, 47, 3.615, 14, 17, 1.214, 14, 3215, 229.643,
            14, 162, 11.571, 14, 1560, 111.429, 13, 28502, 2192.462, 14, 956, 68.286,
            11, 6143, 558.455, 11, 4691, 426.455, 11, 4952, 450.182, 10, 4555,
            455.5, 1, 688, 688.0, 3, 883, 294.333]
        exp2 = [28, 27, 140, 5.185, 24, 95, 3.958, 26, 41, 1.577, 26, 7193, 276.654,
            26, 352, 13.538, 26, 3458, 133.0, 24, 55724, 2321.833, 26, 3021, 116.192,
            18, 10562, 586.778, 17, 6644, 390.824, 18, 7972, 442.889, 17, 7590,
            446.471, 3, 2026, 675.333, 6, 1659, 276.5]
        exp1 = [ str(num) for num in exp1 ]
        exp2 = [ str(num) for num in exp2 ]
        expRow1.extend(exp1)
        expRow2.extend(exp2)
        parseCSV("example2.csv")

        with open("out.csv", 'r') as csvOutput:
            reader = csv.reader(csvOutput, delimiter=',', quotechar='"')
            row0 = next(reader)
            gotRow1 = next(reader)
            gotRow2 = next(reader)
            self.assertEqual(expRow1, gotRow1)
            self.assertEqual(expRow2, gotRow2)

if __name__ == '__main__':
    unittest.main()
