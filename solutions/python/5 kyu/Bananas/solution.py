def bananas_gen(s: str, expected: str = 'banana'):
    if not expected:
        yield "-" * len(s)
    else:
        for i, c in enumerate(s):
            if c == expected[0]:
                start = '-' * i + c
                yield from (start + part for part in bananas_gen(s[i + 1:], expected[1:]))


def bananas(s):
    return [*bananas_gen(s)]