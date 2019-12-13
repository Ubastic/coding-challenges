def last_digit(n1, n2):
    last_number = last = n1 % 10
    numbers = []
    for i in range(1, n2):
        last = (last_number * last) % 10
        if last in numbers:
            return numbers[(n2 - i - 1) % len(numbers)]
        else:
            numbers.append(last)

    return last if n2 != 0 else 1