let solve = board => {
    for (let i = 0; i < 4; i++)
        for (let j = 0; j < 4; j++)
            if (!board[i][j]) {
                let [row, column] = [i - i % 2, j - j % 2];
                let values = [
                    ...board[i],
                    ...board.map(a => a[j]),
                    board[row][column],
                    board[row][column + 1],
                    board[row + 1][column],
                    board[row + 1][column + 1],
                ].filter((a, i, self) => a !== 0 && self.indexOf(a) === i)

                if (values.length === 3) {
                    [1, 2, 3, 4].filter(v => !values.includes(v)).forEach(v => board[i][j] = v);
                    return solve(board);
                }
            }

    return board.reduce((arr, a) => [...arr, ...a], []).some(i => !i) ? "This sudoku is unsolvable!" : board;
}