def find_missing_letter(chars):
    return ''.join({*map(chr, range(ord(chars[0]), ord(chars[-1])))} - {*chars})
