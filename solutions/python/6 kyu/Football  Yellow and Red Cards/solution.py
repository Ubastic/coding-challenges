def men_still_standing(cards):
    d = {'A': {str(i + 1): [] for i in range(11)}, 'B': {str(i + 1): [] for i in range(11)}}
    for t, *n, c in cards:
        n = ''.join(n)
        if (c == 'R' or 'Y' in d[t].get(n, ())) and d[t].get(n) is not None:
            del d[t][n]
        elif n in d[t]:
            d[t][n].append(c)
        if len(d[t]) < 7:
            break

    return len(d['A']), len(d['B'])