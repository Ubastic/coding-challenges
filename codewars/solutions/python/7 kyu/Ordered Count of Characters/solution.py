def ordered_count(input):
    used ,arr = set(),list()
    
    for s in input:
        if s not in used:
            arr.append((s, input.count(s)))
            used.add(s)
            
    return arr