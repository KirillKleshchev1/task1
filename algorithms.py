import time
import memory_profiler


class Mode:
    def time_check(self: str, pattern: str, search) -> time:
        """
        Функция для просмотра времени работы алгоритма.
        Принимает строку и подстроку, алгоритм поиска.
        Возвращает время работы алгоритма.
        """
        start = time.time()
        search(self, pattern)
        return time.time() - start

    @memory_profiler.profile
    def memory_check(self: str, pattern: str, search) -> str:
        """
        Функция для просмотра использования памяти алгоритма.
        Принимает строку и подстроку, алгоритм поиска.
        Возвращает сколько памяти, использует алгоритм.
        """
        search(self, pattern)
        return 'Использование памяти алгоритмом'


class Prefix:
    def prefix_function(self: str) -> list:
        """
        Вспомогательная функция для алгоритма Кнутта-Мориса-Пратта,
        которая позволяет находить максимальный префикс строки.
        Принимает строку.
        Возвращает максимальный префикс строки.
        """
        string_len = len(self)
        prefix = [0] * string_len
        for i in range(1, string_len):
            last_char_largest_prefix = prefix[i - 1]
            while last_char_largest_prefix > 0 and \
                    self[i] != self[last_char_largest_prefix]:
                last_char_largest_prefix = prefix[last_char_largest_prefix - 1]
            if self[i] == self[last_char_largest_prefix]:
                last_char_largest_prefix += 1
            prefix[i] = last_char_largest_prefix
        return prefix


class SearchAlgo:
    def kmp(self: str, pattern: str) -> list:
        """
        Функция, реализующая алгоритм Кнутта-Мориса-Пратта.
        Принимает строку и подстроку.
        Возвращает все вхождения подстроки в строку.
        """
        string_len, pattern_len = len(self), len(pattern)
        prefix = Prefix.prefix_function(pattern)
        current_prefix = 0
        result = []
        for i in range(string_len):
            while current_prefix > 0 and \
                    self[i] != pattern[current_prefix]:
                current_prefix = prefix[current_prefix - 1]
            if self[i] == pattern[current_prefix]:
                current_prefix += 1
            if current_prefix == pattern_len:
                result.append(i - pattern_len + 1)
                current_prefix = prefix[current_prefix - 1]
        return result

    def boyer_moore(self: str, pattern: str) -> list:
        """
        Функция, реализующая алгоритм Бойера-Мура.
        Принимает строку и подстроку.
        Возвращает все вхождения подстроки в строку.
        """
        string_len, pattern_len = len(self), len(pattern)
        if pattern_len == 0:
            return []
        last = {}
        for current_char_pattern in range(pattern_len):
            last[pattern[current_char_pattern]] = current_char_pattern
        current_char_string = pattern_len - 1
        current_char_pattern = pattern_len - 1
        result = []
        while current_char_string < string_len:
            if self[current_char_string] == pattern[current_char_pattern]:
                if current_char_pattern == 0:
                    result.append(current_char_string)
                    current_char_string += pattern_len
                    current_char_pattern = pattern_len - 1
                else:
                    current_char_string -= 1
                    current_char_pattern -= 1
            else:
                last_occurrence_char = last.get(self[current_char_string], -1)
                current_char_string += pattern_len - \
                    min(current_char_pattern, last_occurrence_char + 1)
                current_char_pattern = pattern_len - 1
        return result

    def rabin_karp(self: str, pattern: str) -> list:
        """
        Функция, реализующая алгоритм Рабина-Карпа.
        Принимает строку и подстроку.
        Возвращает все вхождения подстроки в строку.
        """
        string_len, pattern_len = len(self), len(pattern)
        if pattern_len > string_len:
            return []

        prime = 31
        pattern_hash = 0
        for char in pattern:
            pattern_hash = pattern_hash * prime + ord(char)
        text_hash = 0
        for i in range(pattern_len):
            text_hash = text_hash * prime + ord(self[i])
        result = []
        for i in range(string_len - pattern_len + 1):
            if text_hash == pattern_hash and self[i:i + pattern_len] == pattern:
                result.append(i)
            if i < string_len - pattern_len:
                text_hash = text_hash - ord(self[i]) * prime ** (pattern_len - 1)
                text_hash = text_hash * prime + ord(self[i + pattern_len])
        return result

    def naive(self: str, pattern: str) -> list:
        """
        Функция, реализующая алгоритм наивного поиска.
        Принимает строку и подстроку.
        Возвращает все вхождения подстроки в строку.
        """
        string_len, pattern_len = len(self), len(pattern)
        result = []
        for i in range(string_len - pattern_len + 1):
            if self[i:i + pattern_len] == pattern:
                result.append(i)
        return result
