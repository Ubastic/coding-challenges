def delete_digit(n):
    s = str(n)
    return max(int(c) for c in (s[:i] + s[i + 1:] for i in range(len(s))) if not c.startswith('0'))
