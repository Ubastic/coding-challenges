from heapq import heappop, heappush

STEPS = (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)


def find_word(board, word):
    queue = [
        (word[1:], (i, j), {(i, j)})
        for i, w in enumerate(board) for j, c in enumerate(w)
        if c == word[0]
    ]

    while queue:
        w, (x, y), visited = heappop(queue)

        if not w:
            return True

        for x_step, y_step in STEPS:
            xx, yy = pos = x + x_step, y + y_step

            if pos not in visited and len(board) > xx >= 0 and len(board[0]) > yy >= 0 and board[xx][yy] == w[0]:
                heappush(queue, (w[1:], pos, visited | {pos}))

    return False