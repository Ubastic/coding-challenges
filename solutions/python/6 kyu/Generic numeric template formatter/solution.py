from itertools import cycle


def numeric_formatter(template, fill='1234567890'):
    n = cycle(fill)
    return ''.join(next(n) if c.isalpha() else c for c in template)
