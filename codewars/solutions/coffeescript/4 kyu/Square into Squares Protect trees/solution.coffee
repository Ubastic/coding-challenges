decompose = (n) => simplifier(n, n * n)?[...-1] ? null

simplifier = (n, others) =>
  return [n] if others is 0

  for i in [n - 1..1]
    break unless i > 0

    if others - (i * i) >= 0
      r = simplifier(i, others - (i * i))
      return [r..., n] if r?