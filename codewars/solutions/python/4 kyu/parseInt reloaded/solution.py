KNOWN_ONE = {
    'zero': '0',
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
}

KNOWN_TWO = {
    'ten': 10,
    'eleven': 11,
    'twelve': 12,
    'thirteen': 13,
    'fourteen': 14,
    'fifteen': 15,
    'sixteen': 16,
    'seventeen': 17,
    'eighteen': 18,
    'nineteen': 19,
    'twenty': 20,
    'thirty': 30,
    'forty': 40,
    'fifty': 50,
    'sixty': 60,
    'seventy': 70,
    'eighty': 80,
    'ninety': 90
}

POWERS = {
    'hundred': 100,
    'thousand': 1000,
    'million': 1000_000
}


def parse_num(s):
    first, second = s.split('-')
    return KNOWN_TWO[first] + KNOWN_ONE[second]


def parse_int(s):
    power, num = 1, 0

    for p in reversed([c for c in s.split() if c != 'and']):
        if p in POWERS:
            power = power * POWERS[p] if POWERS[p] < power else POWERS[p]
        else:
            num += int(KNOWN_ONE.get(p) or KNOWN_TWO.get(p) or parse_num(p)) * power

    return num
