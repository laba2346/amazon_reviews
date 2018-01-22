import unittest
import sys
import os
sys.path.append('..')

from main import buildMRC, scoreReview
from word import Word
sys.path.append('..')


class TestReviewScoring(unittest.TestCase):
    def test_review(self):
        os.chdir("/Users/landon/Dropbox/Amazon project/")
        words = buildMRC("1054/mrc2.dct")
        #Here, our expected is derived by manually searching the DB for each (reduced) review
        #and scoring it. The results of this manual labor can be found in scoreReviewTest.xlsxs
        exp = [16, 16, 73, 4.562, 13, 47, 3.615, 14, 17, 1.214, 14, 3215, 229.643,
            14, 162, 11.571, 14, 1560, 111.429, 13, 28502, 2192.462, 14, 956, 68.286,
            11, 6143, 558.455, 11, 4691, 426.455, 11, 4952, 450.182, 10, 4555,
            455.5, 1, 688, 688.0, 3, 883, 294.333]
        got = scoreReview(words, "The hose attachment has to be placed on when you want to use it and my bare floor tool was missing. Looks nice and the floor options seems to work ok.")
        self.assertEqual(exp, got)

    def test_another_review(self):
        os.chdir("/Users/landon/Dropbox/Amazon project/")
        words = buildMRC("1054/mrc2.dct")
        exp = [15, 15, 78, 5.2, 12, 44, 3.667, 12, 16, 1.333, 12, 3105, 258.75, 12,
            157, 13.083, 12, 1654, 137.833, 12, 19731, 1644.25, 15, 1880, 125.333,
            9, 5122, 569.111, 7, 3087, 441.0, 9, 3625, 402.778, 7, 3178, 454.0,
            0, 0, 0, 0, 0, 0]
        got = scoreReview(words, "This is a solid PHONE! DEFINITELY. I really enjoyed using it. Not a huge fan of the screen... but I can make it work. The best phone ever, really!")
        self.assertEqual(exp, got)

    def test_scoring_nonsense(self):
        #Score a review where none of the words are going to be found in the db.
        #Should return a zero for every score except original word count.
        os.chdir("/Users/landon/Dropbox/Amazon project/")
        words = buildMRC("1054/mrc2.dct")
        exp = [0]*43
        exp[0] = 3
        got = scoreReview(words, "dis nu NUUU 123")
        self.assertEqual(exp, got)

    def test_review3(self):
        os.chdir("/Users/landon/Dropbox/Amazon project/")
        words = buildMRC("1054/mrc2.dct")
        exp = [12, 12, 66, 5.5, 8, 33, 4.125, 9, 12, 1.333, 9, 3162, 351.333, 9,
            121, 13.444, 9, 1587, 176.333, 9, 20739, 2304.333, 11, 724, 65.818,
            8, 4531, 566.375, 8, 3336, 417.0, 8, 3504, 438.0, 6, 2634, 439.0, 0,
            0, 0, 4, 1441, 360.25]
        got = scoreReview(words, "a great case. hard to take off!... BUT the protection makes up for it. Thanks! :)\nI'll definitely purchase a case from these guys again.")
        self.assertEqual(exp, got)

if __name__ == '__main__':
    unittest.main()
