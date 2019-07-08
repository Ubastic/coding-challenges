import numpy
digits = set(range(1, 10))

def validSolution(board):
    board = numpy.array(board)
    if not (all(set(a) == digits for a in board) and all(set(a) == digits for a in board.T)):
        return False

    for i in range(3):
        for j in range(3):
            if board[i * 3:(i + 1) * 3, j * 3:(j + 1) * 3].sum() != sum(digits):
                return False
    return True