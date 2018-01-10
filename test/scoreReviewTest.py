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
        exp = [16, 16, 77, 4.812, 13, 49, 3.769, 13, 17, 1.308, 13, 2589, 199.154, 13, 145, 11.154, 13, 1279, 98.385, 11, 27083, 2462.091, 14, 949, 67.786, 9, 5003, 555.889, 9, 4042,
            449.111, 9, 4274, 474.889, 8, 3754, 469.25, 1, 688, 688.0, 3, 839, 279.667]
        got = scoreReview(words, "The hose attachment has to be placed on when you want to use it and my bare floor tool was missing. Looks nice and the floor options seems to work ok.")
        self.assertEqual(exp, got)

    def test_scoring_nonsense(self):
        #Score a review where none of the words are going to be found in the db.
        #Should return a zero for every score except original word count.
        os.chdir("/Users/landon/Dropbox/Amazon project/")
        words = buildMRC("1054/mrc2.dct")
        exp = [0]*43
        exp[0] = 3
        got = scoreReview(words, "dis nu 123")
        self.assertEqual(exp, got)
if __name__ == '__main__':
    unittest.main()
