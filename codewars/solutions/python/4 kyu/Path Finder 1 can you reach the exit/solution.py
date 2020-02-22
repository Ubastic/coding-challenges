STEPS = ((-1, 0,), (1, 0), (0, -1), (0, 1))


def can_go(arr: list, x: int, y: int) -> bool:
    try:
        return x >= 0 and y >= 0 and arr[x][y] != 'W'
    except IndexError:
        return False


def path_finder(maze):
    arr = [[*s] for s in maze.splitlines(False)]
    arr[0][0] = 'W'
    queue = [(0, 0)]

    while queue:
        x, y = queue.pop(0)

        if x == y == len(arr) - 1:
            return True

        for x_step, y_step in STEPS:
            xx, yy = x + x_step, y + y_step

            if can_go(arr, xx, yy):
                arr[xx][yy] = 'W'
                queue.append((xx, yy))

    return False