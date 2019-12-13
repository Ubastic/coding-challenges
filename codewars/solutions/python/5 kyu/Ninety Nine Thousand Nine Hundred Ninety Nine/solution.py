def number_to_english(n):
    numbers = {
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
        10: 'ten',
        11: 'eleven',
        12: 'twelve',
        13: 'thirteen',
        14: 'fourteen',
        15: 'fifteen',
        16: 'sixteen',
        17: 'seventeen',
        18: 'eighteen',
        19: 'nineteen',
        20: 'twenty',
        30: 'thirty',
        40: 'forty',
        50: 'fifty',
        60: 'sixty',
        70: 'seventy',
        80: 'eighty',
        90: 'ninety'
    }

    if n < 0 or isinstance(n, float) or n > 99999:
        return ''

    if n == 0:
        return 'zero'

    def convert_to_str(number):
        s = []
        if number:
            if number in numbers:
                return numbers[number]

            decimal = number // 10 * 10
            digit = number % 10

            if decimal:
                s.append(numbers[decimal])
            if digit:
                s.append(numbers[digit])

        return ' '.join(s) if s else ''

    result = []

    twenty = convert_to_str(n % 100)
    n //= 100
    hundreds = convert_to_str(n % 10)
    n //= 10
    thousand = convert_to_str(n)

    if thousand:
        result.append(thousand + ' thousand')
    if hundreds:
        result.append(hundreds + ' hundred')
    if twenty:
        result.append(twenty)

    return ' '.join(result)
