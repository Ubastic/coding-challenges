class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

def reverse(head, prev=None):
    if head:
        node = Node(head.data)
        node.next = prev
        return reverse(head.next, node)
    return prev
