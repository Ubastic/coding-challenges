def scramble(s1, s2):
    if len(s2) > len(s1):
        return False
    if s1 in s2:
        return True   

    return all(s1.count(s) >= s2.count(s) for s in set(s2))