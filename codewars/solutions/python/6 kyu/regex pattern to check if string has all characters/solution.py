def regex_contains_all(st): 
    return f'.*{"".join(rf"(?=.*{s})" for s in st)}.*';