def sort_string(s, o):
    return ''.join(
        sorted(filter(lambda i: i in o, s),key=o.index) 
        + [*filter(lambda i: i not in o, s)]
    )