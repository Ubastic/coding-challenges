class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return

        rows, columns = len(board), len(board[0])
        to_modify = {(i, j) for j in range(columns) for i in range(rows)}

        queue = [(i, j) for j in (0, columns - 1) for i in range(rows) if board[i][j] == 'O']
        queue.extend((i, j) for j in range(columns) for i in (0, rows - 1) if board[i][j] == 'O')
        visited = {*queue}

        while queue:
            i, j = queue.pop()

            for x_diff, y_diff in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                ii, jj = i + x_diff, j + y_diff

                if 0 <= ii < rows and 0 <= jj < columns and (ii, jj) not in visited and board[ii][jj] == 'O':
                    visited.add((ii, jj))
                    queue.append((ii, jj))

        for i, j in to_modify - visited:
            board[i][j] = 'X'
