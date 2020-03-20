anyLineEqual = (board, piece) ->
  board.some (b) -> b.every (p) -> p is piece

rotate = (board) ->
  board[0].map((col, i) -> board.map((row) -> row[i]))

diagonal = (board, reversed = false) ->
  [board.map (b, i) -> board[i][if reversed then b.length - 1 - i else i]]

isSolvedFor = (board, player) ->
  anyLineEqual(board, player) or
  anyLineEqual(rotate board, player) or
  anyLineEqual(diagonal board, player) or
  anyLineEqual(diagonal(board, false), player)

isSolved = (board) ->
  if isSolvedFor(board, 1)
    1
  else if isSolvedFor(board, 2)
    2
  else if (board.some (b) -> b.some (c) -> c is 0)
    -1
  else
    0