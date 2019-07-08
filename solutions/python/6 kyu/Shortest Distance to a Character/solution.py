def shortest_to_char(s, c):
    if not c or not s or c not in s:
        return []
    indexes = [i for i, cc in enumerate(s) if cc == c]
    return [0 if cc == c else min(max(i - j, j - i) for j in indexes) for i, cc in enumerate(s)]
