def find_E(s):
    if not s:
        return s
    
    count_of_e = s.lower().count('e')
    return str(count_of_e) if count_of_e else 'There is no "e".'