from itertools import groupby

def uniq(seq):
    return [s for s, _ in groupby(seq)]