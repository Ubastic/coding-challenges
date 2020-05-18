def search(titles, term):
    return [t for t in titles if term in t.lower()]