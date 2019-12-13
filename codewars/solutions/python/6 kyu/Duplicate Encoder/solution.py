def duplicate_encode(word):
    return ''.join('(' if word.lower().count(c) == 1 else ')' for c in word.lower())