def find_in_array(seq, predicate): 
    return next((i for i, v in enumerate(seq) if predicate(v, i)), -1)