largestDifference = (data) ->
  max = 0
  for i in [0..data.length]
    for j in [i + 1..data.length]
      max = j - i if j - i > max and data[i] <= data[j]

  return max