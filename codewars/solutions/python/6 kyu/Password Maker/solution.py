from itertools import chain
from string import ascii_lowercase as al, ascii_uppercase as au, digits as ad


def make_password(length, u, l, d):
    ss = [[*s] for s, b in zip((al, au, ad), (l, u, d)) if b]
    return ''.join(s.pop() for s in ss) + ''.join(s for s, _ in zip(chain(*ss), range(length - len(ss))))
