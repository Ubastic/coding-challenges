KEYBOARD = {
    c: (j, i)
    for i, a in enumerate(("abcde123", "fghij456", "klmno789", "pqrst.@0", "uvwxyz_/", '* '))
    for j, c in enumerate(a)
}


def chars(words: str):
    shift = False
    for c in words:
        if c.isalpha() and (c.isupper() and not shift or c.islower() and shift):
            shift = not shift
            yield '*'
        yield c


def tv_remote(words) -> int:
    start_pos, clicks = (0, 0), 0
    for c in chars(words):
        clicks += sum(map(lambda a, b: max(a, b) - min(a, b), KEYBOARD[c.lower()], start_pos)) + 1
        start_pos = KEYBOARD[c.lower()]
    return clicks