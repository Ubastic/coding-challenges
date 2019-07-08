import re

REGEX = re.compile(r'^(?=[MDCLXVI])M*(C[MD]|D?C{0,3})(X[CL]|L?X{0,3})(I[XV]|V?I{0,3})$')


def valid_romans(arr):
    return [a for a in arr if REGEX.match(a)]
