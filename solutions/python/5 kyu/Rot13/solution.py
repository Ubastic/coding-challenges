import string
from codecs import encode as _dont_use_this_

l = [chr(c) for c in range(ord('a'), ord('z') + 1)]
u = [c.upper() for c in l]

def rot13(m):
    return ''.join((u * c.isupper() or l)[(l.index(c.lower()) + 13) % len(l)] if c.isalpha() else c for c in m)
