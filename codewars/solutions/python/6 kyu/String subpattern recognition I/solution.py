import re

def has_subpattern(string):
    return re.match(r'^(.+)\1+$', string) is not None