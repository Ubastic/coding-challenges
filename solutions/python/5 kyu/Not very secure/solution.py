def alphanumeric(s):
    return s and all(c.isalpha() or c.isdigit() for c in s)
