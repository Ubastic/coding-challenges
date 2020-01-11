def visit(t, current, end, path, paths, weight=0):
    for v, w in t[current].items():
        if v in path:
            continue
        elif v == end:
            paths.append([[*path, v], weight + w])
        else:
            visit(t, v, end, [*path, v], paths, weight + w)


def shortestPath(t, start, end):
    paths = []
    visit(t, start, end, [start], paths)

    min_w, min_p = min((w, len(p)) for p, w in paths)
    return sorted(p for p, w in paths if w == min_w and len(p) == min_p)