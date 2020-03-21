from heapq import heappop, heappush

STEPS = [(2, -1), (2, 1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]


def normalize(x, y):
    return 'abcdefgh'.index(x), int(y) - 1


def knight(p1, p2):
    src, dst = normalize(*p1), normalize(*p2)

    queue = [(0, src)]
    visited = {src}

    while queue:
        distance, (x, y) = heappop(queue)

        if (x, y) == dst:
            return distance

        for xd, yd in STEPS:
            xx, yy = x + xd, y + yd

            if 0 <= xx < 8 and 0 <= yy < 8 and (xx, yy) not in visited:
                visited.add((xx, yy))
                heappush(queue, (distance + 1, (xx, yy)))