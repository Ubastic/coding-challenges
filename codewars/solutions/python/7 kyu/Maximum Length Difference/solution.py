def mxdiflg(a1, a2):
    max_len = -1
    for i in a1:
        for j in a2:
            max_len = max(max_len, abs(len(i) - len(j)))

    return max_len