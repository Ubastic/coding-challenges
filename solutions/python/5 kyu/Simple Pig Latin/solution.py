def pig_it(text):
    return ' '.join(map(lambda s: (s[1:] + s[0] + 'ay') if s.isalpha() else s, text.split()))