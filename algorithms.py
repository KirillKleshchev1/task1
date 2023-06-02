import time
import memory_profiler
from abc import ABC, abstractmethod

PRIME_NUMBER = 31


class Parser(ABC):
    """
    Класс Парсер
    """

    def __init__(self, string: str, pattern: str):
        if string is None or isinstance(string, bytes):
            raise TypeError("Invalid input for string")
        if pattern is None or isinstance(pattern, bytes):
            raise TypeError("Invalid input for pattern")

        self.string = string
        self.pattern = pattern

    @abstractmethod
    def search_method(self) -> list:
        pass

    @staticmethod
    def prefix_function(string: str) -> list:
        """
        Вспомогательная функция для алгоритма Кнутта-Мориса-Пратта,
        которая позволяет находить максимальный префикс строки.
        Принимает строку.
        Возвращает максимальный префикс строки.
        """
        string_len = len(string)
        prefix = [0] * string_len
        for i in range(1, string_len):
            last_char_largest_prefix = prefix[i - 1]
            while last_char_largest_prefix > 0 and string[i] != string[last_char_largest_prefix]:
                last_char_largest_prefix = prefix[last_char_largest_prefix - 1]
            if string[i] == string[last_char_largest_prefix]:
                last_char_largest_prefix += 1
            prefix[i] = last_char_largest_prefix
        return prefix


class Mode:
    """
    Функция для просмотра времени работы алгоритма.
    Принимает строку и подстроку, алгоритм поиска.
    Возвращает время работы алгоритма.
    """

    @staticmethod
    def time_check(func: Parser) -> time:
        start = time.time()
        func.search_method()
        return time.time() - start

    @staticmethod
    @memory_profiler.profile
    def memory_check(func: Parser) -> None:
        """
        Функция для просмотра использования памяти алгоритма.
        Принимает строку и подстроку, алгоритм поиска.
        Возвращает количество памяти, используемое алгоритмом (в МБ).
        """
        func.search_method()


class Kmp(Parser):
    def search_method(self) -> list:
        """
        Функция, реализующая алгоритм Кнутта-Мориса-Пратта.
        Принимает строку и подстроку.
        Возвращает все вхождения подстроки в строку.
        """
        string_len, pattern_len = len(self.string), len(self.pattern)
        prefix = self.prefix_function(self.string)
        current_prefix = 0
        result = []
        for i in range(string_len):
            while current_prefix > 0 and \
                    self.string[i] != self.pattern[current_prefix]:
                current_prefix = prefix[current_prefix - 1]
            if self.string[i] == self.pattern[current_prefix]:
                current_prefix += 1
            if current_prefix == pattern_len:
                result.append(i - pattern_len + 1)
                current_prefix = prefix[current_prefix - 1]
        return result


class BoyerMoore(Parser):
    def search_method(self) -> list:
        """
        Функция, реализующая алгоритм Бойера-Мура.
        Принимает строку и подстроку.
        Возвращает все вхождения подстроки в строку.
        """
        string_len, pattern_len = len(self.string), len(self.pattern)
        if pattern_len == 0:
            return []
        last = {}
        for current_char_pattern in range(pattern_len):
            last[self.pattern[current_char_pattern]] = current_char_pattern
        current_char_string = pattern_len - 1
        current_char_pattern = pattern_len - 1
        result = []
        while current_char_string < string_len:
            if self.string[current_char_string] == self.pattern[current_char_pattern]:
                if current_char_pattern == 0:
                    result.append(current_char_string)
                    current_char_string += pattern_len
                    current_char_pattern = pattern_len - 1
                else:
                    current_char_string -= 1
                    current_char_pattern -= 1
            else:
                last_occurrence_char = last.get(self.string[current_char_string], -1)
                current_char_string += pattern_len - \
                    min(current_char_pattern, last_occurrence_char + 1)
                current_char_pattern = pattern_len - 1
        return result


class RabinKarp(Parser):
    def search_method(self) -> list:
        """
        Функция, реализующая алгоритм Рабина-Карпа.
        Принимает строку и подстроку.
        Возвращает все вхождения подстроки в строку.
        """
        string_len, pattern_len = len(self.string), len(self.pattern)
        if pattern_len > string_len:
            return []

        pattern_hash = 0
        for char in self.pattern:
            pattern_hash = pattern_hash * PRIME_NUMBER + ord(char)
        text_hash = 0
        for i in range(pattern_len):
            text_hash = text_hash * PRIME_NUMBER + ord(self.string[i])
        result = []
        for i in range(string_len - pattern_len + 1):
            if text_hash == pattern_hash and self.string[i:i + pattern_len] == self.pattern:
                result.append(i)
            if i < string_len - pattern_len:
                text_hash = text_hash - ord(self.string[i]) * PRIME_NUMBER ** (pattern_len - 1)
                text_hash = text_hash * PRIME_NUMBER + ord(self.string[i + pattern_len])
        return result


class Naive(Parser):
    def search_method(self) -> list:
        """
        Функция, реализующая алгоритм наивного поиска.
        Принимает строку и подстроку.
        Возвращает все вхождения подстроки в строку.
        """
        string_len, pattern_len = len(self.string), len(self.pattern)
        result = []
        for i in range(string_len - pattern_len + 1):
            if self.string[i:i + pattern_len] == self.pattern:
                result.append(i)
        return result
