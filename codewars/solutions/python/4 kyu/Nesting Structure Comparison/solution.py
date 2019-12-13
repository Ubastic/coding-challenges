def same_structure_as(original, other):
    f = lambda a: [{'arr': f(i)} for i in a] if hasattr(a, '__iter__') else [{'val': True}]
    return isinstance(original, type(other)) and f(original) == f(other)
