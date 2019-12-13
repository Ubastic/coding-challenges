def bits(s):
    for *data, parity in s.split():
        if sum(int(b) for b in data) % 2 != int(parity):
            yield 'error'
        else:
            yield ''.join(data)


def parity_bit(binary):
    return ' '.join(bits(binary))