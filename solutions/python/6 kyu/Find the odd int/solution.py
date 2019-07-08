def find_it(seq):
    return next(n for n in seq if seq.count(n) % 2)