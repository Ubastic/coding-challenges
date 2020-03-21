Array::nonEmpty = -> @ if @length

Array::flat = -> @reduce ((acc, a) => [acc..., a...]), []

Array::sorted = (predicate) -> @[..].sort(predicate)

Array::groupBy = (grouper, other...) ->
  return @ unless grouper?

  groups = {}
  order = []

  for row in @
    group = grouper row

    unless (order.some (i) => i is group)
      order.push group

    groups[group] ?= []
    groups[group].push row

  order.map (group) => [group, groups[group].groupBy(other...)]

Array::applyPredicates = (allPredicates) -> @filter (row) =>
  allPredicates.every (predicates) => predicates.some (w) => w row

joined = (first, others...) ->
  return [] unless first?

  toJoin = joined(others...)
  first.map (row) => toJoin.nonEmpty()?.map((join) => [row, join...]) ? [row]

class Query
  constructor: (@_select, @_from, @_gropby, @_orderby, @_where = [], @_having = []) ->

  @api: (propToCheck, f) -> () ->
    if propToCheck? and @["_#{propToCheck}"] != undefined
      throw Error("Duplicate #{propToCheck.toUpperCase()}")

    f.apply @, arguments
    @

  from    :@api "from"    ,(from...)            -> @_from    = from
  groupBy :@api "groupby" ,(groupers...)        -> @_groupby = groupers
  select  :@api "select"  ,(selector   = null)  -> @_select  = selector
  orderBy :@api "orderby" ,(comparator = null)  -> @_orderby = comparator
  where   :@api null      ,(predicates...)      -> @_where.push  predicates
  having  :@api null      ,(predicates...)      -> @_having.push predicates

  execute: () ->
    joined (@_from ? [])...
      .flat()
      .applyPredicates @_where
      .groupBy         (@_groupby ? [])...
      .applyPredicates @_having
      .sorted          (@_orderby ? ((a, b) => 0))
      .map             (row) => (@_select ? ((a) => (a))) row

query = -> new Query