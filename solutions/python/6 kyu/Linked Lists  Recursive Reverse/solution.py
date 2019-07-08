class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None


def walk(head):
    while head:
        yield head.data
        head = head.next


def add(node, data=None):
    n = Node(data)
    node.next = n
    return n


def reverse(h):
    if not h:
        return None

    head = temp = None
    for i in reversed([*walk(h)]):
        if head is None:
            temp = head = Node(i)
        else:
            temp = add(temp, i)

    return head