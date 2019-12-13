def camel_case(string):
    return ''.join(s.title() for s in string.strip().split())