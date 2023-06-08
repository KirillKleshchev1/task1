import unittest
from algorithms import Kmp, RabinKarp, BoyerMoore, Naive
from main import TYPES_MODE


class TestTest(unittest.TestCase):
    def test_kmp(self):
        algorithm_object = Kmp("aba", "a")
        self.assertEqual(algorithm_object.search_method(), [0, 2])

    def test_kmp_not_pattern(self):
        algorithm_object = Kmp('aba', 'c')
        self.assertEqual(algorithm_object.search_method(), [])

    def test_kmp_pattern_longer_text(self):
        algorithm_object = Kmp("a", "aba")
        self.assertEqual(algorithm_object.search_method(), [])

    def test_boyer_moore(self):
        algorithm_object = BoyerMoore("aba", "a")
        self.assertEqual(algorithm_object.search_method(), [0, 2])

    def test_boyer_moore_not_pattern(self):
        algorithm_object = BoyerMoore("aba", "c")
        self.assertEqual(algorithm_object.search_method(), [])

    def test_boyer_moore_pattern_longer_text(self):
        algorithm_object = BoyerMoore("c", "aba")
        self.assertEqual(algorithm_object.search_method(), [])

    def test_rk(self):
        algorithm_object = RabinKarp("aba", "a")
        self.assertEqual(algorithm_object.search_method(), [0, 2])

    def test_rk_not_pattern(self):
        algorithm_object = RabinKarp("aba", "c")
        self.assertEqual(algorithm_object.search_method(), [])

    def test_rk_pattern_longer_text(self):
        algorithm_object = RabinKarp("c", "aba")
        self.assertEqual(algorithm_object.search_method(), [])

    def test_native(self):
        algorithm_object = Naive("aba", "a")
        self.assertEqual(algorithm_object.search_method(), [0, 2])

    def test_naive_not_pattern(self):
        algorithm_object = Naive("aba", "c")
        self.assertEqual(algorithm_object.search_method(), [])

    def test_naive_pattern_longer_text(self):
        algorithm_object = Naive("c", "aba")
        self.assertEqual(algorithm_object.search_method(), [])

    def test_types_mode(self):
        algorithm_object = Kmp('aba', 'a')
        assert TYPES_MODE['time_check'](algorithm_object) == 0.0

    def test_kmp_invalid_input_None(self):
        with self.assertRaises(TypeError):
            Kmp(None, 'a')

    def test_boyer_moore_invalid_input_Bytes(self):
        with self.assertRaises(TypeError):
            BoyerMoore("aba", b'a')

    def test_rk_invalid_input_bytes(self):
        with self.assertRaises(TypeError):
            RabinKarp(b'aba', 'a')

    def test_naive_invalid_input_None(self):
        with self.assertRaises(TypeError):
            Naive('aba', None)

    def test_kmp_invalid_input_float(self):
        with self.assertRaises(TypeError):
            Kmp('aba', 2.34)

    def test_naive_invalid_input_bool(self):
        with self.assertRaises(TypeError):
            Naive(True, 'a')

    def test_boyer_moore_invalid_input_list(self):
        with self.assertRaises(TypeError):
            BoyerMoore('aa', [1, 2])
