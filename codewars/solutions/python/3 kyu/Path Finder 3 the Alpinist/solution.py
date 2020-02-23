def path_finder(maze):
    arr = [[[int(i), float('inf')] for i in s] for s in maze.splitlines(False)]
    arr[0][0][1] = 0

    queue = [(0, 0, arr[0][0][0])]
    while queue:
        x, y, value = queue.pop(0)

        for x_step, y_step in ((-1, 0,), (1, 0), (0, -1), (0, 1)):
            xx, yy = x + x_step, y + y_step

            if 0 <= xx < len(arr) and 0 <= yy < len(arr):
                val, cell_total = arr[xx][yy]
                new_cell_total = arr[x][y][1] + abs(value - val)

                if new_cell_total < cell_total:
                    arr[xx][yy][1] = new_cell_total
                    queue.append((xx, yy, val))

    return arr[-1][-1][1]