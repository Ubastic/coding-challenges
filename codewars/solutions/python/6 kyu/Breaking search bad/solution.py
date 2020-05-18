def search(titles, term): 
    return list(filter(lambda title: term in title.lower(), titles))