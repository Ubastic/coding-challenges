from itertools import count


def find_num_factory():
    numbers, numbers_list = list(range(11)), list(range(10))
    numbers_set = set(numbers_list)

    cache, not_used_numbers = {}, []

    def get_digits(num):
        digits = set()

        while num:
            digits.add(num % 10)
            num //= 10

        return digits

    def generate_numbers(numbers_count, is_first=True):
        if numbers_count == 0:
            for num in numbers_list:
                yield num, {num}
        else:
            for i in numbers_list:
                if is_first and i == 0:
                    continue

                key = tuple((i, numbers_count))

                if key in cache:
                    yield from cache[key]
                else:
                    arr = []
                    for j in generate_numbers(numbers_count - 1, False):
                        value = (i * 10 ** numbers_count + j[0], set({i}.union(j[1])))

                        yield value

                        arr.append(value)

                    cache[key] = arr

    def gen():
        for i in count(1):
            yield from generate_numbers(i)

    gen_iter = iter(gen())
    next(gen_iter)

    def wrapp(n):
        numbers_len = len(numbers)
        if n <= 10 or n < numbers_len:
            return numbers[n]
        i = numbers[-1]

        for _ in range(n - numbers_len + 1):
            numbers_digits = numbers_set - get_digits(i)

            def find():
                for j, (num, dgts) in enumerate(not_used_numbers):
                    if dgts.issubset(numbers_digits):
                        return not_used_numbers.pop(j)[0]

                for num, dgts in gen_iter:
                    if dgts.issubset(numbers_digits):
                        return num
                    else:
                        not_used_numbers.append((num, dgts))

            i = find()
            numbers.append(i)

        return i

    return wrapp


find_num = find_num_factory()
