values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, }


def solution(roman):
    value, max_val = 0, 1
    for i in map(lambda key: values[key], reversed(roman)):
        value += -i if i < max_val else i
        max_val = max((max_val, i))
    return value
