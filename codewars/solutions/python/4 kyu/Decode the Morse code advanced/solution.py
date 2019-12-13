import re


def decodeBits(bits):
    bits = bits.strip('0')
    part_len = len(min(re.findall(r'0+|1+', bits), key=len)) * 2
    max_len = part_len * 2

    def gen(part):
        for word in re.split(r'(?<=1)0{' + str(part_len) + ',}(?=1)', part) or part:
            yield '.' if set(part) == {'1'} else re.sub(r'1+', '.', re.sub(r'1{' + str(part_len or 1) + ',}', '-', word)).replace('0', '')

    return '   '.join(' '.join(gen(c)) for c in re.split(r'(?<=1)[0]{' + str(max_len) + ',}(?=1)', bits) or bits)


def decodeMorse(m):
    return ' '.join(''.join(MORSE_CODE.get(c) for c in w.split()) for w in re.split(r'(?<=[.-])[ ]{3,}(?=[.-])', m))
