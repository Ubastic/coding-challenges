def arithmetic_sequence_elements(a, r, n):
    result = []
    for i in xrange(n):
        result.append(str(a))
        a += r
    
    return ", ".join(result)