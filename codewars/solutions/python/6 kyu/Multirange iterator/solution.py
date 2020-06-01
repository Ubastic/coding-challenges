def multiiter(*p):
    if p and all(p):
        next_demension = [*multiiter(*p[1:])] or [()]
        yield from ((i, *n) for i in range(p[0]) for n in next_demension)