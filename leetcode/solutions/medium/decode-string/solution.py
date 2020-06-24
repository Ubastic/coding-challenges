from re import compile, Match

REGEX = compile(r'(\d+)\[([^\[]*?)\]')


def on_match(match: Match) -> str:
    count, value = match.groups()
    return value * int(count)


class Solution:
    def decodeString(self, s: str) -> str:
        while '[' in s:
            s = REGEX.sub(on_match, s)
        return s