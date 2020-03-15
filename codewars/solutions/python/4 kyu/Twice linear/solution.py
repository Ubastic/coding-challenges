from heapq import heappop, heappush


def dbl_linear(n):
    heap, u = [], 1

    for _ in range(n):
        heappush(heap, 2 * u + 1)
        heappush(heap, 3 * u + 1)

        u = heappop(heap)

        if u == heap[0]:
            heappop(heap)

    return u
