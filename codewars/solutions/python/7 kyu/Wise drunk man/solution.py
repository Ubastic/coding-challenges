import re

def wdm(talk):
    return re.sub("\s+", " ", re.sub("puke|hiccup", "", talk)).strip()