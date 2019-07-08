def solve(s):
    if s == s[::-1]:
        return "OK"

    for i in range(len(s)):
        new_str = s[:i] + s[i + 1:]
        if new_str == new_str[::-1]:
            return "remove one"

    return "not possible"
