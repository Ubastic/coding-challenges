import re

DIGITS_REGEX = re.compile(r'\d+$')

def increment_string(strng):
    digits = DIGITS_REGEX.search(strng)
    if not digits:
        return strng + '1'
    digits = digits.group() 
    number = str(int(digits) + 1)
    return '{}{}{}'.format(strng.replace(digits, ''), '0' * (len(digits) - len(number)), number)