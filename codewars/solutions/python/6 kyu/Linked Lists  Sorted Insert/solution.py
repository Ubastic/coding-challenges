def sorted_insert(head, data):
    if head is None:
        return Node(data)

    node = head
    prev = None
    while node:
        if node.data > data:
            n = Node(data)
            if prev is None:
                head, n.next = n, head
            else:
                prev.next, n.next = n, node
            break

        prev, node = node, node.next
    else:
        prev.next = Node(data)

    return head