def string_expansion(s):
    a, n = [], 1
    for c in s:
        if c.isdigit():
            n = int(c)
        else:
            a.append(c * n)
    return ''.join(a)