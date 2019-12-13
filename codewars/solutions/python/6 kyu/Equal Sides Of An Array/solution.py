def find_even_index(arr):
    return next((i for i in range(len(arr)) if sum(arr[:i]) == sum(arr[i + 1:])), -1)