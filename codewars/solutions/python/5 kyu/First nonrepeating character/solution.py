def first_non_repeating_letter(s):
    return next((c for c in s if s.lower().count(c.lower()) == 1), '')
