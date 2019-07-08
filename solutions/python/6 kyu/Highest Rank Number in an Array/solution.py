def highest_rank(arr):
    return max(sorted(set(arr), reverse=True), key=arr.count)