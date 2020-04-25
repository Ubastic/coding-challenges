import re

def to_underscore(s):
    if not isinstance(s, str):
        return str(s)
    return re.sub(r'(?<!^)(?=[A-Z])', '_', s).lower()