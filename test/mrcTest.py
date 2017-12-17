import unittest
import sys
sys.path.append('..')

from main import buildMRC
from word import Word

class TestMRCImport(unittest.TestCase):
    def test_able(self):
        words = buildMRC("testMRC.dct")
        exp = Word(4, 0, 1, 216, 15, 167, 930, 66, 575, 302, 284, 355, 0, 0)
        got = words["ABLE"]
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

    def test_ablush(self):
        words = buildMRC("testMRC.dct")
        exp = Word(6, 0, 2, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0, 0)
        got = words["ABLUSH"]
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

    def test_abdomen(self):
        words = buildMRC("testMRC.dct")
        exp = Word(7, 7, 3, 6, 5, 6, 49, 0, 426 , 586, 548, 0, 475, 556)
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

if __name__ == '__main__':
    unittest.main()
