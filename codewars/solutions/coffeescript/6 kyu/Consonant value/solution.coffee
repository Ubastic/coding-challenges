solve = (s) ->
  Math.max.apply @,
    s.split(/[aeiou]+/g)
      .filter Boolean
      .map (part) -> [part...].map((c) -> c.charCodeAt() - 'a'.charCodeAt() + 1)
      .map (part) -> part.reduce (a, b) -> a + b