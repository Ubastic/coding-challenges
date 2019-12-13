def search_substr(f, s, o=True):
    return 0 if not f or not s or s not in f else 1 + search_substr(f[f.index(s) + (1 if o else len(s)):], s, o)
