def to_list(head):
    arr = []
    while head:
        arr.append(head.data)
        head = head.next
    return arr


def to_llist(arr):
    if not arr:
        return None
    head = node = Node(arr[0])
    for a in arr[1:]:
        node.next = Node(a)
        node = node.next
    return head


def insert_sort(head):
    return to_llist(sorted(to_list(head)))
