partitionOn = (pred, items) ->
  [trues, falses] = [[], []]
  items.forEach (c) ->
    (if pred(c) then trues else falses).push c

  items.length = 0
  items.push falses..., trues...

  falses.length