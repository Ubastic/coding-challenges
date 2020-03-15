from heapq import heappop, heappush


def hamming(n):
    heap = [1]

    for _ in range(n - 1):
        h = heappop(heap)

        while heap and h == heap[0]:
            heappop(heap)

        for m in (2, 3, 5):
            heappush(heap, m * h)

    return heappop(heap)