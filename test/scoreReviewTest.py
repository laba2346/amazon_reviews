import unittest
import sys
sys.path.append('..')

from main import buildMRC, scoreReview
from word import Word
sys.path.append('..')


class TestReviewScoring(unittest.TestCase):
    def test_review(self):
        words = buildMRC("mrc2.dct")
        #Here, our expected is derived by manually searching the DB for each (reduced) review
        #and scoring it. The results of this manual labor can be found in scoreReviewTest.xlsxs
        exp = [63, 48, 17, 72161, 145, 1569, 254340, 7531, 5021, 3903, 4088, 3534, 688, 614]
        got = scoreReview(words, "The hose attachment has to be placed on when you want to use it and my bare floor tool was missing. Looks nice and the floor options seems to work ok.")
        self.assertEqual(exp, got)

    def test_scoring_nonsense(self):
        #Score a review where none of the words are going to be found in the db.
        #Should return a zero for every score except original word count.
        words = buildMRC("mrc2.dct")
        exp = [0]*43
        exp[0] = 3
        got = scoreReview(words, "dis nu 123")
        self.assertEqual(exp, got)
if __name__ == '__main__':
    unittest.main()
