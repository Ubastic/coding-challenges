def prime_string(s):
    return all(s[:i] * (len(s) // i) != s for i in range(1, len(s) // 2 + 1))
