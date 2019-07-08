def sort_array(a):
    odd = sorted(i for i in a if i % 2)
    even = sorted((i for i in a if not i % 2), reverse=True)

    return [(odd if i % 2 else even).pop(0) for i in a]
