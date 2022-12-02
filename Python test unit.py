from main import line
import unittest

class TestReverse(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(line(""),"")

    def test_one_sym(self):
        self.assertEqual(line("a"), "a")

    def test_polindrom(self):
        self.assertEqual(line("aba"), "aba")

    def test_correct(self):
        self.assertEqual(line("abcd"), "dcba")

    def test_type_int(self):
        with self.assertRaises(TypeError):
            line(42)

    def test_type_list(self):
        with self.assertRaises(TypeError):
            line('c', 'a', 'd')


if __name__ == '__main__':
    unittest.main()
