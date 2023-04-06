import unittest
import algorithms
import main


class TestTest(unittest.TestCase):
    def test_kmp(self):
        self.assertEqual(algorithms.SearchAlgo.kmp('aba', 'a'), [0, 2])

    def test_kmp_not_pattern(self):
        self.assertEqual(algorithms.SearchAlgo.kmp('aba', 'c'), [])

    def test_kmp_pattern_longer_text(self):
        self.assertEqual(algorithms.SearchAlgo.kmp('c', 'aba'), [])

    def test_boyer_moore(self):
        self.assertEqual(algorithms.SearchAlgo.boyer_moore('aba', 'a'), [0, 2])

    def test_boyer_moore_not_pattern(self):
        self.assertEqual(algorithms.SearchAlgo.boyer_moore('aba', 'c'), [])

    def test_boyer_moore_pattern_longer_text(self):
        self.assertEqual(algorithms.SearchAlgo.boyer_moore('c', 'aba'), [])

    def test_rk(self):
        self.assertEqual(algorithms.SearchAlgo.rabin_karp('aba', 'a'), [0, 2])

    def test_rk_not_pattern(self):
        self.assertEqual(algorithms.SearchAlgo.rabin_karp('aba', 'c'), [])

    def test_rk_pattern_longer_text(self):
        self.assertEqual(algorithms.SearchAlgo.rabin_karp('c', 'aba'), [])

    def test_native(self):
        self.assertEqual(algorithms.SearchAlgo.naive('aba', 'a'), [0, 2])

    def test_naive_not_pattern(self):
        self.assertEqual(algorithms.SearchAlgo.naive('aba', 'c'), [])

    def test_naive_pattern_longer_text(self):
        self.assertEqual(algorithms.SearchAlgo.naive('c', 'aba'), [])

    def test_types_algo_kmp(self):
        self.assertEqual(main.TYPES_ALGO['kmp']('aba', 'a'), [0, 2])

    def test_types_algo_rabin_karp(self):
        self.assertEqual(main.TYPES_ALGO['rabin_karp']('aba', 'a'), [0, 2])

    def test_types_algo_boyer_moore(self):
        self.assertEqual(main.TYPES_ALGO['boyer_moore']('aba', 'a'), [0, 2])

    def test_types_algo_naive(self):
        self.assertEqual(main.TYPES_ALGO['naive']('aba', 'a'), [0, 2])

    def test_types_mode(self):
        self.assertEqual(main.TYPES_MODE['time_check']('aba', 'a', main.TYPES_ALGO['kmp']), 0.0)
