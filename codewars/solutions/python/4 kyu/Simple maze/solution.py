def has_exit(maze):
    queue = [(i, j) for i, a in enumerate(maze) for j, c in enumerate(a) if c == 'k']
    assert len(queue) == 1
    visited = {*queue}

    while queue:
        x, y = queue.pop()

        if x in (0, len(maze) - 1) or y in (0, len(maze[0]) - 1):
            return True

        for x_step, y_step in (1, 0), (0, 1), (-1, 0), (0, -1):
            xx, yy = pos = x + x_step, y + y_step

            if pos not in visited and len(maze) > xx >= 0 and len(maze[0]) > yy >= 0 and maze[xx][yy] == ' ':
                visited.add(pos)
                queue.append(pos)

    return False