def huffman(p):
    if len(p) == 2:
        return dict(zip(p, ('0', '1')))

    a1, a2, *_ = sorted(p, key=lambda k: p[k])
    p_copy = {**p}
    p_copy[a1 + a2] = p_copy.pop(a1) + p_copy.pop(a2)

    c = huffman(p_copy)
    ca1a2 = c.pop(a1 + a2)
    return {**c, a1: ca1a2 + '0', a2: ca1a2 + '1'}

def encode(freqs, s):
    if len(freqs) <= 1:
        return None

    tree = huffman(dict(freqs))
    return ''.join(tree[c] for c in s)

def decode(freqs, bits):
    if len(freqs) <= 1:
        return None

    tree = {v: k for k, v in huffman(dict(freqs)).items()}

    key, res = '', []
    for c in bits:
        key += c
        if key in tree:
            res.append(tree[key])
            key = ''

    return ''.join(res)

def frequencies(s):
    return [(c, s.count(c)) for c in set(s)]