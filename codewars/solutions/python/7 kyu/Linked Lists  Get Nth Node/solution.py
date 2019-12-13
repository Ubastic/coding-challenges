def get_nth(node, index, current=0):
    assert current <= index and node is not None
    return get_nth(node.next, index, current + 1) if index != current else node
