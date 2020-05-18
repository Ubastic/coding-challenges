from itertools import groupby

def uniq_c(seq): 
    return [(c, len([*g])) for c, g in groupby(seq)]