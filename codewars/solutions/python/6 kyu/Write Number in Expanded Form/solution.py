def expanded_form(num):
    return ' + '.join(c + '0' * (len(str(num)) - i) for i, c in enumerate(str(num), 1) if c != '0')
