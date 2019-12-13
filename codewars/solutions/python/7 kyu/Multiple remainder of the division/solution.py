def isMultiple(a, b, n):
    if a % b == 0:
        return False

    number = str(float(a) / b).split('.')[-1]
    add = 0
    num = 0

    for i in reversed(number):
        num = int(i) + add

        add = num >= 5

    num = num % 10

    return num % n == 0 and num != 0

