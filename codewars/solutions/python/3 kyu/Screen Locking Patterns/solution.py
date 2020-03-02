INTERSECTIONS = ['ABC', 'ADG', 'AEI', 'BEH', 'CEG', 'CFI', 'DEF', 'GHI']
INTERSECTIONS.extend(s[::-1] for s in INTERSECTIONS[:])

POINTS = {*'ABCDEFGHI'}
DEFAULT = dict.fromkeys(POINTS, frozenset())

EFFECTS = {p: {**DEFAULT} for p in POINTS}
FORBIDDEN = {p: {**DEFAULT} for p in POINTS}

for a, b, c in INTERSECTIONS:
    EFFECTS[a][c] = {b}
    FORBIDDEN[c][b] = {a}


def count_patterns_from(point, l, path=None, forbidden=frozenset()):
    if not (path or 0 < l < 10):
        return 0

    path = path or {point}

    if len(path) == l:
        return 1
    if len(path) > l:
        return 0

    return sum(
        count_patterns_from(p, l, path | {p} | EFFECTS[point][p], FORBIDDEN[point][p])
        for p in POINTS - path - forbidden
    )