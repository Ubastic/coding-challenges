def findNextCellToFill(grid, i, j):
    for x in range(i, 9):
        for y in range(j, 9):
            if grid[x][y] == 0:
                return x, y
    for x in range(0, 9):
        for y in range(0, 9):
            if grid[x][y] == 0:
                return x, y
    return -1, -1


def isValid(grid, i, j, e):
    if all(e != grid[i][x] for x in range(9)) and all(e != grid[x][j] for x in range(9)):
        sec_top_x, sec_top_y = 3 * (i // 3), 3 * (j // 3)

        for x in range(sec_top_x, sec_top_x + 3):
            for y in range(sec_top_y, sec_top_y + 3):
                if grid[x][y] == e:
                    return False
        return True
    return False


def sudoku(grid, i=0, j=0):
    i, j = findNextCellToFill(grid, i, j)

    if i == -1:
        return grid

    for e in range(1, 10):
        if isValid(grid, i, j, e):
            grid[i][j] = e
            if sudoku(grid, i, j) is not None:
                return grid
            grid[i][j] = 0