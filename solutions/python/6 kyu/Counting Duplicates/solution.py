def duplicate_count(text):
    text = text.lower()
    return sum(text.count(t) > 1 for t in set(text))
     