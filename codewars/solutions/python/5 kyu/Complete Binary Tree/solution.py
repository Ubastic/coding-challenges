import math
from itertools import chain


def divide_on_parts(arr):
    nodes = len(arr)

    if nodes == 1:
        return [], arr[0], []

    height = math.ceil(math.log2(nodes + 1))
    min_branch = 2 ** (height - 2) - 1
    max_branch = 2 ** (height - 1) - 1

    left_count = min(max_branch, nodes - 1 - min_branch) + 1
    (*left, head), right = arr[:left_count], arr[left_count:]

    return left, head, right


def insert(visit, array):
    if array:
        visit.append(array)


def complete_binary_tree(a):
    visit = [a]
    results = [[]]
    count = 1

    while visit:
        arr = visit.pop(0)

        left, head, right = divide_on_parts(arr)
        results[-1].append(head)
        count -= 1

        if count == 0:
            count = 2 ** len(results)
            results.append([])

        insert(visit, left)
        insert(visit, right)

    return list(chain(*results))