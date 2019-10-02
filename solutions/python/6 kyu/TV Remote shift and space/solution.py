KEYBOARD = ("abcde123", "fghij456", "klmno789", "pqrst.@0", "uvwxyz_/", '* ')


def index_of(c: str):
    c = c.lower()
    for i, keys in enumerate(KEYBOARD):
        if c in keys:
            return keys.index(c), i


def diff(a: int, b: int) -> int:
    return max(a, b) - min(a, b)


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
        next_pos = index_of(c)
        clicks, start_pos = clicks + sum(map(diff, next_pos, start_pos)) + 1, next_pos

    return clicks