def insert_nth(head, index, data):
    if not index:
        n = Node(data)
        n.next = head
        return n

    head.next = insert_nth(head.next, index - 1, data)
    return head