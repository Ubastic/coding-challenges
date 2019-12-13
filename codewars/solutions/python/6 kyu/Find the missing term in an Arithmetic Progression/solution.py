def find_missing(s):
    daley = min(abs(b - a) for a, b in zip(s, s[1:]))

    if s[0] < s[1]:
        return next(a + daley for a, b in zip(s, s[1:]) if abs(b - a) != daley)
    else:
        return next(a - daley for a, b in zip(s, s[1:]) if abs(b - a) != daley)