from functools import lru_cache


@lru_cache()
def count_subsequences(pattern: str, s: str) -> int:
    if not pattern or len(pattern) > len(s):
        return 0
    elif len(pattern) == 1:
        return s.count(pattern[0])

    return sum(count_subsequences(pattern[1:], s[i + 1:]) for i, c in enumerate(s) if c == pattern[0])
