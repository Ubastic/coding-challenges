def score_throws(r):
    return sum(10 if i < 5 else 5 if 5 <= i <= 10 else 0 for i in r) + 100 * bool(all(i < 5 for i in r) and r)
