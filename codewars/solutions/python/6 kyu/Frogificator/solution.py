import re


def frogify(s):
    s = re.sub(r'[,;()-]', '', s)
    s = re.sub(r'\s+', ' ', s)
    sentences = filter(bool, re.split(r'[.!?]', s))
    limiters = filter(bool, re.findall(r'[.!?]', s))

    result = ""

    for sentence, limiter in zip(sentences, limiters):
        result += " ".join(reversed(sentence.split())) + limiter + " "

    return result[:-1]