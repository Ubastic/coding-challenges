def first_dup(s):
    return next((c for c in s if s.count(c) > 1), None)