import re

def to_camel_case(text):
    return text[0] + re.sub('-|_','',text.title())[1:] if text else text