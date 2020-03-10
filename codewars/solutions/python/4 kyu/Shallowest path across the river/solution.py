from heapq import heapify, heappop, heappush

STEPS = [(-1, 1), (0, 1), (1, 1), (-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0)]
NOT_SEEN = float("inf"), 0


def shallowest_path(river):
    height, width = len(river), len(river[0])

    seen = {(x, 0): (0, None) for x, _ in enumerate(river)}
    queue = [(cost, 0, (x, 0)) for x, (cost, *_) in enumerate(river)]
    heapify(queue)

    while queue:
        max_deep, cost, (x, y) = heappop(queue)

        if y == width - 1:
            path, node = [], (x, y)
            while node:
                path.append(node)
                _, node = seen[node]

            return path[::-1]

        for x_step, y_step in STEPS:
            xx, yy = next_pos = x + x_step, y + y_step

            if 0 <= xx < height and 0 <= yy < width:
                next_cost = cost + 1

                if seen.get(next_pos, NOT_SEEN)[0] > next_cost:
                    seen[next_pos] = next_cost, (x, y)
                    heappush(queue, (max(max_deep, river[xx][yy]), next_cost, next_pos))
