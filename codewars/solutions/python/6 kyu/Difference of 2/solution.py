def twos_difference(lst): 
    return sorted(tuple(sorted((a, b))) for i, a in enumerate(lst) for b in lst[i+1:] if abs(a - b) == 2)