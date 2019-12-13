def get_middle(s):
    return s[len(s) / 2] if len(s) % 2 else s[len(s) / 2 - 1:len(s) / 2 + 1]
