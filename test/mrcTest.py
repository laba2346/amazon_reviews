import unittest
import sys
sys.path.append('..')

from main import buildMRC, extractWord
from word import Word

class TestMRCImport(unittest.TestCase):
    def test_seem(self):
        words = buildMRC("testMRC.dct")
        exp = Word(4, 3, 1, 229, 15, 154, 4577, 48, 549, 226, 249, 325, 0, 0)
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

    def test_seek(self):
        words = buildMRC("testMRC.dct")
        exp = Word(4, 3, 1, 69, 13, 57, 288, 0, 506, 375, 335, 412, 0, 0)
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

    def test_extractSeem(self):
        exp = "SEEM"
        got = extractWord("0403100229151540045770048549226249325000000 VV S   SEEM|sim|sim|0")
        self.assertEqual(exp, got)

    def test_extractSeed(self):
        exp = "SEED"
        got = extractWord("0403100041090140002840000514611542467000000 NN S  BSEED|sid|sid|0")
        self.assertEqual(exp, got)

if __name__ == '__main__':
    unittest.main()
