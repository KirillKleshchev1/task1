import unittest
import main


class TestTest(unittest.TestCase):
    def test_kmp(self):
        self.assertEqual(main.kmp('aba', 'a'), [0, 2])

    def test_kmp_not_pattern(self):
        self.assertEqual(main.kmp('aba', 'c'), [])

    def test_kmp_pattern_longer_text(self):
        self.assertEqual(main.kmp('c', 'aba'), [])

    def test_boyer_moore(self):
        self.assertEqual(main.boyer_moore('aba', 'a'), [0, 2])

    def test_boyer_moore_not_pattern(self):
        self.assertEqual(main.boyer_moore('aba', 'c'), [])

    def test_boyer_moore_pattern_longer_text(self):
        self.assertEqual(main.boyer_moore('c', 'aba'), [])

    def test_rk(self):
        self.assertEqual(main.rabin_karp('aba', 'a'), [0, 2])

    def test_rk_not_pattern(self):
        self.assertEqual(main.rabin_karp('aba', 'c'), [])

    def test_rk_pattern_longer_text(self):
        self.assertEqual(main.rabin_karp('c', 'aba'), [])

    def test_native(self):
        self.assertEqual(main.naive('aba', 'a'), [0, 2])

    def test_naive_not_pattern(self):
        self.assertEqual(main.naive('aba', 'c'), [])

    def test_naive_pattern_longer_text(self):
        self.assertEqual(main.naive('c', 'aba'), [])
