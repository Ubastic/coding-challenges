from heapq import heapify, heappop, heappush


def closure_gen(*s):
    heap = [*s]
    heapify(heap)
    numbers = {*s}

    while heap:
        n = heappop(heap)

        yield n

        to_add = {n * i for i in s} - numbers
        numbers |= to_add

        for n in to_add:
            heappush(heap, n)