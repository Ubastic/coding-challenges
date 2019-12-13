import re

DIGITS_REGEX = re.compile('\d+')

def order(sentence):
    return ' '.join(sorted(sentence.split(), key=lambda a:int(DIGITS_REGEX.search(a).group())))