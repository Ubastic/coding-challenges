def insert_nth(head, index, data):
    if not head and index == 0:
        return Node(data)

    prev = None
    node = head
    for i in range(index):
        assert node is not None
        prev = node
        node = node.next

    n = Node(data)
    if prev:
        prev.next = n
    else:
        head = n
    n.next = node

    return head