from heapq import heappop, heappush

NOT_SEEN = float("inf"), 0

STEPS = {
    "down": (1, 0),
    "right": (0, 1),
    "left": (0, -1),
    "up": (-1, 0),
}


def cheapest_path(arr, start, finish):
    seen = {start: (0, None)}
    queue = [(0, start)]

    while queue and queue[0][1] != finish:
        cost, (x, y) = heappop(queue)
        next_cost = cost + arr[x][y]

        for direction, (x_step, y_step) in STEPS.items():
            xx, yy = next_pos = x + x_step, y + y_step

            if (
                    0 <= xx < len(arr) and
                    0 <= yy < len(arr[0]) and
                    seen.get(next_pos, NOT_SEEN)[0] >= next_cost
            ):
                seen[next_pos] = next_cost, direction
                heappush(queue, (next_cost, next_pos))

    path = []
    node = finish
    while node != start:
        _, direction = seen[node]

        path.append(direction)

        x, y = node
        x_step, y_step = STEPS[direction]
        node = x - x_step, y - y_step

    return path[::-1]
