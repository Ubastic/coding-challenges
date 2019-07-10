def point(a, b):
    def inner(): pass

    inner.fst = a
    inner.snd = b
    return inner


def fst(pt):
    return pt.fst


def snd(pt):
    return pt.snd


def sqr_dist(pt1, pt2):
    return (pt1.fst - pt2.fst) ** 2 + (pt1.snd - pt2.snd) ** 2


def line(pt1, pt2):
    a = pt2.fst - pt1.fst
    b = pt1.snd - pt2.snd
    c = a * pt2.snd + b * pt2.fst
    return [b, a, -c]
