import unittest
import sys
import os
sys.path.append('..')

from main import isNumber
from word import Word
sys.path.append('..')

class TestHelperFunctions(unittest.TestCase):
    def test_isNumber1(self):
        self.assertFalse(isNumber("."))
        self.assertFalse(isNumber("b"))
        self.assertFalse(isNumber(""))
        self.assertFalse(isNumber("Hello world!"))
        self.assertTrue(isNumber("123"))
        self.assertTrue(isNumber("1"))
        self.assertTrue(isNumber("012"))

if __name__ == '__main__':
    unittest.main()
