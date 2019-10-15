def numbers(digits, start=1):
    if digits == 1:
        for i in range(start, 10):
            yield str(i)
    else:
        for i in range(start, 10):
            for j in numbers(digits - 1, i):
                yield str(i) + j


def find_all(sum_dig, digs):
    if sum(map(int, str(int('1' + '0' * digs) - 1))) < sum_dig:
        return []

    min_num = max_num = None
    counter = 0
    for i in numbers(digs):
        if sum(map(int, i)) == sum_dig:
            if min_num is None:
                min_num = i
            max_num = i
            counter += 1

    return [counter, int(min_num), int(max_num)]