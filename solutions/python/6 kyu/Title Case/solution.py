def title_case(title, minor_words=''):
    minor_words, title = minor_words.lower().split(), title.lower()
    return ' '.join(c.title() if c not in minor_words or not i else c.lower() for i, c in enumerate(title.split()))
