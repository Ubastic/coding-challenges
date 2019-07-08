def in_array(array1, array2):
    return list(sorted(set(filter(lambda a: any(a in s for s in array2), array1))))