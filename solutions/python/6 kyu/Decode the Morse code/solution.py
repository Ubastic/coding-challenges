import re


def decodeMorse(morse_code):
    s = []
    for word in re.split(r'(?<=[.-])[ ]{2,}(?=[.-])', morse_code):
        s.append(''.join(MORSE_CODE.get(c) for c in word.split()))
    return ' '.join(s)
