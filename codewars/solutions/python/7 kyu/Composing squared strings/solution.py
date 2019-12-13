def compose(s1, s2):
    s1, s2 = s1.split(), s2.split()
    n = len(s1[0])

    return "\n".join(s[0][:i] + s[1][:n - i + 1] for i, s in enumerate(zip(s1, reversed(s2)), 1))