def sort_array(source_array):
    odds = sorted(i for i in source_array if i % 2)
    return [odds.pop(0) if i % 2 else i for i in source_array]
