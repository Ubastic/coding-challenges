import numpy
digits = set(range(1, 10))

def done_or_not(board):
    board = numpy.array(board)
    if not (all(set(a) == digits for a in board) and all(set(a) == digits for a in board.T)):
        return 'Try again!'

    for i in range(3):
        for j in range(3):
            if board[i * 3:(i + 1) * 3, j * 3:(j + 1) * 3].sum() != sum(digits):
                return 'Try again!'
    return 'Finished!'