def braces_status(s):
    s = ''.join(c for c in s if c in '(){}[]')
    while '{}' in s or '()' in s or '[]' in s:
        s = s.replace('{}', '').replace('[]', '').replace('()', '')
    return not s