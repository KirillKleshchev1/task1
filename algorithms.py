import time
import memory_profiler


class Mode:
    def time_check(self: str, pattern: str, search) -> time:
        """Функция для просмотра времени работы алгоритма.
                        Принимает строку и подстроку, алгоритм поиска.
                        Возвращает время работы алгоритма."""
        start = time.time()
        search(self, pattern)
        return time.time() - start

    @memory_profiler.profile
    def memory_check(self: str, pattern: str, search) -> str:
        """Функция для просмотра использования памяти алгоритма.
                                Принимает строку и подстроку, алгоритм поиска.
                                Возвращает сколько памяти, использует алгоритм."""
        search(self, pattern)
        return 'Использование памяти алгоритмом'


class Prefix:
    def prefix_function(self: str) -> list:
        """Вспомогательная функция для алгоритма Кнутта-Мориса-Пратта,
                которая позволяет находить максимальный префикс строки.
                Принимает строку.
                Возвращает максимальный префикс строки."""
        n = len(self)
        prefix = [0] * n
        for i in range(1, n):
            j = prefix[i - 1]
            while j > 0 and self[i] != self[j]:
                j = prefix[j - 1]
            if self[i] == self[j]:
                j += 1
            prefix[i] = j
        return prefix


class SearchAlgo:
    def kmp(self: str, pattern: str) -> list:
        """Функция, реализующая алгоритм Кнутта-Мориса-Пратта.
                Принимает строку и подстроку.
                Возвращает все вхождения подстроки в строку."""
        n = len(self)
        m = len(pattern)
        prefix = Prefix.prefix_function(pattern)
        j = 0
        result = []
        for i in range(n):
            while j > 0 and self[i] != pattern[j]:
                j = prefix[j - 1]
            if self[i] == pattern[j]:
                j += 1
            if j == m:
                result.append(i - m + 1)
                j = prefix[j - 1]
        return result

    def boyer_moore(self: str, pattern: str) -> list:
        """Функция, реализующая алгоритм Бойера-Мура.
                        Принимает строку и подстроку.
                        Возвращает все вхождения подстроки в строку."""
        n, m = len(self), len(pattern)
        if m == 0:
            return []
        last = {}
        for k in range(m):
            last[pattern[k]] = k
        i = m - 1
        k = m - 1
        result = []
        while i < n:
            if self[i] == pattern[k]:
                if k == 0:
                    result.append(i)
                    i += m
                    k = m - 1
                else:
                    i -= 1
                    k -= 1
            else:
                j = last.get(self[i], -1)
                i += m - min(k, j + 1)
                k = m - 1
        return result

    def rabin_karp(self: str, pattern: str) -> list:
        """Функция, реализующая алгоритм Рабина-Карпа.
                        Принимает строку и подстроку.
                        Возвращает все вхождения подстроки в строку."""
        if len(pattern) > len(self):
            return []

        prime = 31
        pattern_hash = 0
        for char in pattern:
            pattern_hash = pattern_hash * prime + ord(char)
        text_hash = 0
        for i in range(len(pattern)):
            text_hash = text_hash * prime + ord(self[i])
        result = []
        for i in range(len(self) - len(pattern) + 1):
            if text_hash == pattern_hash and self[i:i + len(pattern)] == pattern:
                result.append(i)
            if i < len(self) - len(pattern):
                text_hash = text_hash - ord(self[i]) * prime ** (len(pattern) - 1)
                text_hash = text_hash * prime + ord(self[i + len(pattern)])
        return result

    def naive(self: str, pattern: str) -> list:
        """Функция, реализующая алгоритм наивного поиска.
                        Принимает строку и подстроку.
                        Возвращает все вхождения подстроки в строку."""
        n = len(self)
        m = len(pattern)
        result = []
        for i in range(n - m + 1):
            if self[i:i + m] == pattern:
                result.append(i)
        return result
