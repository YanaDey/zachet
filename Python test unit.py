import unittest
from main import count_vowels
class TestReverse(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(count_vowels(''), '')
