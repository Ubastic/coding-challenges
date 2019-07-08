def generate_numbers(numbers, numbers_count):
    if numbers_count == 0:
        yield from numbers
    else:
        new_numbers_count = numbers_count - 1

        for i in numbers:
            for j in generate_numbers(numbers, new_numbers_count):
                number = i * 10 ** numbers_count + j

                yield number


def find_num(n):
    if n <= 10:
        return n

    numbers = list(range(11))
    numbers_set = set(range(10))

    i = 10

    for _ in range(n - 10):
        digits = set()
        ii = i
        while ii:
            digits.add(ii % 10)
            ii //= 10

        numbers_digits = sorted(numbers_set - digits)

        def find_number():
            for j in range(1, len(numbers_digits) + 1):
                for num in generate_numbers(numbers_digits, j):
                    if num not in numbers:
                        return num

        number = find_number()
        numbers.append(number)
        i = number

    return numbers[-1]