fibgen = ->
  [a, b] = [0, 1]
  loop
    yield a
    [a, b] = [b, a + b]

genfib = ->
  f = fibgen()
  -> f.next().value