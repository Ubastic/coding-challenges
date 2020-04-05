import re

def solution(s):
    return re.sub(r"(?=[A-Z])", " ", s)