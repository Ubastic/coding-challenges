from itertools import count


def find_nb(m):
    for i in count(1):
        m -= i ** 3
        if m == 0:
            return i
        elif m < 0:
            return -1
