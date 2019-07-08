class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def push(head, data):
    n = Node(data)
    n.next = head
    return n


def build_one_two_three():
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n1.next = n2
    n2.next = n3
    return n1
