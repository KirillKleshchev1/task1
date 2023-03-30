import sys
import time
import memory_profiler


def time_check(text: str, pattern: str, search) -> time:
    start = time.time()
    search(text, pattern)
    return time.time() - start


@memory_profiler.profile
def memory_check(text: str, pattern: str, search) -> str:
    search(text, pattern)
    return 'Использование памяти алгоритмом'


def prefix_function(s: str) -> list:
    n = len(s)
    prefix = [0] * n
    for i in range(1, n):
        j = prefix[i - 1]
        while j > 0 and s[i] != s[j]:
            j = prefix[j - 1]
        if s[i] == s[j]:
            j += 1
        prefix[i] = j
    return prefix


def kmp(text: str, pattern: str) -> list:
    n = len(text)
    m = len(pattern)
    prefix = prefix_function(pattern)
    j = 0
    result = []
    for i in range(n):
        while j > 0 and text[i] != pattern[j]:
            j = prefix[j - 1]
        if text[i] == pattern[j]:
            j += 1
        if j == m:
            result.append(i - m + 1)
            j = prefix[j - 1]
    return result


def boyer_moore(text: str, pattern: str) -> list:
    n, m = len(text), len(pattern)
    if m == 0:
        return []
    last = {}
    for k in range(m):
        last[pattern[k]] = k
    i = m - 1
    k = m - 1
    result = []
    while i < n:
        if text[i] == pattern[k]:
            if k == 0:
                result.append(i)
                i += m
                k = m - 1
            else:
                i -= 1
                k -= 1
        else:
            j = last.get(text[i], -1)
            i += m - min(k, j + 1)
            k = m - 1
    return result


def rabin_karp(text: str, pattern: str) -> list:
    if len(pattern) > len(text):
        return []

    prime = 31
    pattern_hash = 0
    for char in pattern:
        pattern_hash = pattern_hash * prime + ord(char)
    text_hash = 0
    for i in range(len(pattern)):
        text_hash = text_hash * prime + ord(text[i])
    result = []
    for i in range(len(text) - len(pattern) + 1):
        if text_hash == pattern_hash and text[i:i+len(pattern)] == pattern:
            result.append(i)
        if i < len(text) - len(pattern):
            text_hash = text_hash - ord(text[i]) * prime**(len(pattern)-1)
            text_hash = text_hash * prime + ord(text[i+len(pattern)])
    return result


def naive(text: str, pattern: str) -> list:
    n = len(text)
    m = len(pattern)
    result = []
    for i in range(n - m + 1):
        if text[i:i+m] == pattern:
            result.append(i)
    return result


if __name__ == '__main__':
    string = sys.argv[1]
    substring = sys.argv[2]
    types = [kmp,
             boyer_moore,
             rabin_karp,
             naive,
             memory_check,
             time_check
             ]

    typ = int(sys.argv[3])
    option = int(sys.argv[4])
    if option == 0:
        print(types[typ - 1](string, substring))
    if option == 1:
        mode = int(sys.argv[5])
        print(types[mode - 1](string, substring, types[typ - 1]))
