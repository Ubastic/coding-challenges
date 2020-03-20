
class SortedList
  constructor: ->
    @arr = []
    @length = 0

  add: (val) ->
    @length++
    for i in [0..@length - 1]
      if val < @arr[i]
        @arr.splice(i, 0, val)
        return

    @arr.push(val)

  get: (i) -> @arr[i]