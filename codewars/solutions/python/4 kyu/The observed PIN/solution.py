neighborhoods = {
    '1': ['2', '4'],
    '2': ['1', '3', '5'],
    '3': ['2', '6'],
    '4': ['1', '5', '7'],
    '5': ['2', '4', '6', '8'],
    '6': ['3', '5', '9'],
    '7': ['4', '8'],
    '8': ['5', '7', '9', '0'],
    '9': ['6', '8'],
    '0': ['8']
}


def get_pins(observed):
    if observed:
        head, *tail = observed
        tail = get_pins(''.join(tail))
        return [i + t for i in [head, *neighborhoods[head]] for t in tail or ['']]