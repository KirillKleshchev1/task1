import unittest
import algorithms
import main


class TestTest(unittest.TestCase):
    def test_kmp(self):
        pars = algorithms.Parser('aba', 'a')
        assert main.TYPE['kmp'](pars) == [0, 2]

    def test_kmp_not_pattern(self):
        pars = algorithms.Parser('aba', 'c')
        assert main.TYPE['kmp'](pars) == []

    def test_kmp_pattern_longer_text(self):
        pars = algorithms.Parser('a', 'aba')
        assert main.TYPE['kmp'](pars) == []

    def test_boyer_moore(self):
        pars = algorithms.Parser('aba', 'a')
        assert main.TYPE['boyer_moore'](pars) == [0, 2]

    def test_boyer_moore_not_pattern(self):
        pars = algorithms.Parser('aba', 'c')
        assert main.TYPE['boyer_moore'](pars) == []

    def test_boyer_moore_pattern_longer_text(self):
        pars = algorithms.Parser('c', 'aba')
        assert main.TYPE['boyer_moore'](pars) == []

    def test_rk(self):
        pars = algorithms.Parser('aba', 'a')
        assert main.TYPE['rabin_karp'](pars) == [0, 2]

    def test_rk_not_pattern(self):
        pars = algorithms.Parser('aba', 'c')
        assert main.TYPE['rabin_karp'](pars) == []

    def test_rk_pattern_longer_text(self):
        pars = algorithms.Parser('c', 'aba')
        assert main.TYPE['rabin_karp'](pars) == []

    def test_native(self):
        pars = algorithms.Parser('aba', 'a')
        assert main.TYPE['naive'](pars) == [0, 2]

    def test_naive_not_pattern(self):
        pars = algorithms.Parser('aba', 'c')
        assert main.TYPE['naive'](pars) == []

    def test_naive_pattern_longer_text(self):
        pars = algorithms.Parser('c', 'aba')
        assert main.TYPE['naive'](pars) == []

    def test_types_mode(self):
        pars = algorithms.Parser('aba', 'a')
        assert main.TYPES_MODE['time_check'](pars, main.TYPE['kmp']) == 0.0
