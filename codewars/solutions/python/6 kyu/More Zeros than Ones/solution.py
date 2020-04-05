def more_zeros(s):
    return [
        c for c in 
        [c for i, c in enumerate(s) if i == s.index(c)]
        if bin(ord(c)).count("0") - 1 > bin(ord(c)).count("1")
    ]