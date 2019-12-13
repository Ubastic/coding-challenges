def solve(s):
    lower = sum(c.istitle() for c in s)
    upper = len(s) - lower
    return s.lower() if lower <= upper else s.upper()