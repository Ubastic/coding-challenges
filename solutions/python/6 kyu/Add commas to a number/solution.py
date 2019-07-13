def commas(num):
    num = round(num, 3)
    return '{:,}'.format(num if num % 1 else int(num))