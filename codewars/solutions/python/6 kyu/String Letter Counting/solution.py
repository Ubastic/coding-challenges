from string import ascii_lowercase as letters

def string_letter_count(s):
    s = s.lower()
    return "".join(f"{s.count(c)}{c}" for c in letters if s.count(c))