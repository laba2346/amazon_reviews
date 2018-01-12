import unittest
import sys
import os
sys.path.append('..')

from main import buildMRC, extractWord
from word import Word

class TestMRCImport(unittest.TestCase):
    def test_seem(self):
        os.chdir("/Users/landon/Dropbox/Amazon project/") #change this to the project directory
        words = buildMRC("test/testMRC.dct")
        exp = Word(4, 3, 1, 229, 15, 154, 4577, 48, 549, 226, 249, 325, 0, 0, 12)
        got = words["SEEM"]
        self.assertEqual(exp.nlet, got.nlet)
        self.assertEqual(exp.nphon, got.nphon)
        self.assertEqual(exp.nsyl, got.nsyl)
        self.assertEqual(exp.kffreq, got.kffreq)
        self.assertEqual(exp.kfcats, got.kfcats)
        self.assertEqual(exp.kfsamps, got.kfsamps)
        self.assertEqual(exp.tlfreq, got.tlfreq)
        self.assertEqual(exp.bfreq, got.bfreq)
        self.assertEqual(exp.fam, got.fam)
        self.assertEqual(exp.conc, got.conc)
        self.assertEqual(exp.imag, got.imag)
        self.assertEqual(exp.meanc, got.meanc)
        self.assertEqual(exp.meanp, got.meanp)
        self.assertEqual(exp.aoa, got.aoa)
        self.assertEqual(exp.numScores, got.numScores)

    def test_seek(self):
        os.chdir("/Users/landon/Dropbox/Amazon project/") #change this to the project directory
        words = buildMRC("test/testMRC.dct")
        exp = Word(4, 3, 1, 69, 13, 57, 288, 0, 506, 375, 335, 412, 0, 0, 11)
        got = words["SEEK"]
        self.assertEqual(exp.nlet, got.nlet)
        self.assertEqual(exp.nphon, got.nphon)
        self.assertEqual(exp.nsyl, got.nsyl)
        self.assertEqual(exp.kffreq, got.kffreq)
        self.assertEqual(exp.kfcats, got.kfcats)
        self.assertEqual(exp.kfsamps, got.kfsamps)
        self.assertEqual(exp.tlfreq, got.tlfreq)
        self.assertEqual(exp.bfreq, got.bfreq)
        self.assertEqual(exp.fam, got.fam)
        self.assertEqual(exp.conc, got.conc)
        self.assertEqual(exp.imag, got.imag)
        self.assertEqual(exp.meanc, got.meanc)
        self.assertEqual(exp.meanp, got.meanp)
        self.assertEqual(exp.aoa, got.aoa)
        self.assertEqual(exp.numScores, got.numScores)

    def test_abdomen(self):
        os.chdir("/Users/landon/Dropbox/Amazon project/") #change this to the project directory
        words = buildMRC("test/testMRC.dct")
        exp = Word(7, 7, 3, 6, 5, 6, 49, 0, 426 , 586, 548, 0, 475, 556, 12)
        got = words["ABDOMEN"]
        self.assertEqual(exp.nlet, got.nlet)
        self.assertEqual(exp.nphon, got.nphon)
        self.assertEqual(exp.nsyl, got.nsyl)
        self.assertEqual(exp.kffreq, got.kffreq)
        self.assertEqual(exp.kfcats, got.kfcats)
        self.assertEqual(exp.kfsamps, got.kfsamps)
        self.assertEqual(exp.tlfreq, got.tlfreq)
        self.assertEqual(exp.bfreq, got.bfreq)
        self.assertEqual(exp.fam, got.fam)
        self.assertEqual(exp.conc, got.conc)
        self.assertEqual(exp.imag, got.imag)
        self.assertEqual(exp.meanc, got.meanc)
        self.assertEqual(exp.meanp, got.meanp)
        self.assertEqual(exp.aoa, got.aoa)
        self.assertEqual(exp.numScores, got.numScores)


    def test_extractSeem(self):
        os.chdir("/Users/landon/Dropbox/Amazon project/") #change this to the project directory
        exp = "SEEM"
        got = extractWord("0403100229151540045770048549226249325000000 VV S   SEEM|sim|sim|0")
        self.assertEqual(exp, got)

    def test_extractSeed(self):
        os.chdir("/Users/landon/Dropbox/Amazon project/") #change this to the project directory
        exp = "SEED"
        got = extractWord("0403100041090140002840000514611542467000000 NN S  BSEED|sid|sid|0")
        self.assertEqual(exp, got)

    def test_completeness_first(self):
        #Here, the word "the" has three entries in the original MRC db.
        #This test checks if MY mrc db has the more complete entry when the
        #most complete entry is the first one of the three.
        os.chdir("/Users/landon/Dropbox/Amazon project/") #change this to the project directory
        words = buildMRC("test/testMRC.dct")
        exp = Word(3, 2, 1, 69971, 15, 500, 236472, 6833, 625, 237, 209, 212, 0, 0, 12)
        got = words["THE"]
        self.assertEqual(exp.nlet, got.nlet)
        self.assertEqual(exp.nphon, got.nphon)
        self.assertEqual(exp.nsyl, got.nsyl)
        self.assertEqual(exp.kffreq, got.kffreq)
        self.assertEqual(exp.kfcats, got.kfcats)
        self.assertEqual(exp.kfsamps, got.kfsamps)
        self.assertEqual(exp.tlfreq, got.tlfreq)
        self.assertEqual(exp.bfreq, got.bfreq)
        self.assertEqual(exp.fam, got.fam)
        self.assertEqual(exp.conc, got.conc)
        self.assertEqual(exp.imag, got.imag)
        self.assertEqual(exp.meanc, got.meanc)
        self.assertEqual(exp.meanp, got.meanp)
        self.assertEqual(exp.aoa, got.aoa)
        self.assertEqual(exp.numScores, got.numScores)

    def test_completeness_second(self):
        os.chdir("/Users/landon/Dropbox/Amazon project/") #change this to the project directory
        #Here, the word "the" has three entries in the original MRC db.
        #This test checks if MY mrc db has the more complete entry when the
        #most complete entry is the second entry of the three.
        words = buildMRC("test/testMRC3.dct")
        exp = Word(3, 2, 1, 69971, 15, 500, 236472, 6833, 625, 237, 209, 212, 0, 0, 12)
        got = words["THE"]
        self.assertEqual(exp.nlet, got.nlet)
        self.assertEqual(exp.nphon, got.nphon)
        self.assertEqual(exp.nsyl, got.nsyl)
        self.assertEqual(exp.kffreq, got.kffreq)
        self.assertEqual(exp.kfcats, got.kfcats)
        self.assertEqual(exp.kfsamps, got.kfsamps)
        self.assertEqual(exp.tlfreq, got.tlfreq)
        self.assertEqual(exp.bfreq, got.bfreq)
        self.assertEqual(exp.fam, got.fam)
        self.assertEqual(exp.conc, got.conc)
        self.assertEqual(exp.imag, got.imag)
        self.assertEqual(exp.meanc, got.meanc)
        self.assertEqual(exp.meanp, got.meanp)
        self.assertEqual(exp.aoa, got.aoa)
        self.assertEqual(exp.numScores, got.numScores)

    def test_completeness_third(self):
        os.chdir("/Users/landon/Dropbox/Amazon project/") #change this to the project directory
        #Here, the word "the" has three entries in the original MRC db.
        #This test checks if MY mrc db has the more complete entry when the
        #most complete entry is the second entry of the three.
        words = buildMRC("test/testMRC2.dct")
        exp = Word(3, 2, 1, 69971, 15, 500, 236472, 6833, 625, 237, 209, 212, 0, 0, 12)
        got = words["THE"]
        self.assertEqual(exp.nlet, got.nlet)
        self.assertEqual(exp.nphon, got.nphon)
        self.assertEqual(exp.nsyl, got.nsyl)
        self.assertEqual(exp.kffreq, got.kffreq)
        self.assertEqual(exp.kfcats, got.kfcats)
        self.assertEqual(exp.kfsamps, got.kfsamps)
        self.assertEqual(exp.tlfreq, got.tlfreq)
        self.assertEqual(exp.bfreq, got.bfreq)
        self.assertEqual(exp.fam, got.fam)
        self.assertEqual(exp.conc, got.conc)
        self.assertEqual(exp.imag, got.imag)
        self.assertEqual(exp.meanc, got.meanc)
        self.assertEqual(exp.meanp, got.meanp)
        self.assertEqual(exp.aoa, got.aoa)
        self.assertEqual(exp.numScores, got.numScores)

    def test_incomplete_entries(self):
        os.chdir("/Users/landon/Dropbox/Amazon project/") #change this to the project directory
        #Make sure that, even though it is essentially an incomplete entry, that
        #"placed" is in our db. The only reason for this is because the original
        #MRC db does not contain a "better" entry; no entry for "placed" is complete
        words = buildMRC("test/testMRC.dct")
        exp = Word(6, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2)
        got = words["PLACED"]
        self.assertEqual(exp.nlet, got.nlet)
        self.assertEqual(exp.nphon, got.nphon)
        self.assertEqual(exp.nsyl, got.nsyl)
        self.assertEqual(exp.kffreq, got.kffreq)
        self.assertEqual(exp.kfcats, got.kfcats)
        self.assertEqual(exp.kfsamps, got.kfsamps)
        self.assertEqual(exp.tlfreq, got.tlfreq)
        self.assertEqual(exp.bfreq, got.bfreq)
        self.assertEqual(exp.fam, got.fam)
        self.assertEqual(exp.conc, got.conc)
        self.assertEqual(exp.imag, got.imag)
        self.assertEqual(exp.meanc, got.meanc)
        self.assertEqual(exp.meanp, got.meanp)
        self.assertEqual(exp.aoa, got.aoa)
        self.assertEqual(exp.numScores, got.numScores)

    def test_word_not_found(self):
        os.chdir("/Users/landon/Dropbox/Amazon project/") #change this to the project directory        
        words = buildMRC("test/testMRC.dct")
        with self.assertRaises(KeyError):
            words["FAKE"]

if __name__ == '__main__':
    unittest.main()
