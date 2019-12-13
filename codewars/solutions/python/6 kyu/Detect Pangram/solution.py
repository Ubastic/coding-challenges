import string


def is_pangram(s):
    return {*s.lower()}.issuperset(string.ascii_lowercase)
