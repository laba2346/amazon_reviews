import unittest
import sys
import os
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
sys.path.append('..')

from main import reduceReview

class TestReduceReview(unittest.TestCase):
    def test_stopwords(self):
        review = "The dog is CUTE."
        exp = ['dog', 'cute']
        got = reduceReview(review)
        self.assertEqual(exp, got)

    def test_cap_stopwords(self):
        exp = []
        got = reduceReview("the")
        self.assertEqual(exp, got)

    def test_cap_stopwords2(self):
        exp = []
        got = reduceReview("tHe")
        self.assertEqual(exp, got)

    def test_cap_stopwords3(self):
        exp = []
        got = reduceReview("THE ")
        self.assertEqual(exp, got)

    def test_cap_stopwords4(self):
        exp = []
        got = reduceReview("The")
        self.assertEqual(exp, got)

    def test_many_stopwords(self):
        exp = []
        got = reduceReview("The, tHe the THE..")
        self.assertEqual(exp, got)

    def test_cap_stemming(self):
        exp = ['dog']
        got = reduceReview("Dogs")
        self.assertEqual(exp, got)

    def test_cap_stemming2(self):
        exp = ['dog']
        got = reduceReview("DOGS")
        self.assertEqual(exp, got)

    def test_cap_stemming3(self):
        exp = ['dog']
        got = reduceReview("dOgs!")
        self.assertEqual(exp, got)

    def test_same_word_stemming(self):
        upper = reduceReview("Dogs")
        lower = reduceReview("dogs")
        self.assertEqual(upper, lower)

    def test_same_word_stemming2(self):
        upper = reduceReview("DOGS!!!")
        lower = reduceReview(" dogs...")
        self.assertEqual(upper, lower)

    def test_punctuation(self):
        exp = []
        got = reduceReview("THE is!!! ")
        self.assertEqual(exp, got)

    def test_many_stopwords(self):
        exp = ["dog"]
        got = reduceReview("THE is! so the THEM dog!.. ourselves TO thEM thE?")

if __name__ == '__main__':
    unittest.main()
