def length(node, l=0):
    return length(node.next, l + 1) if node else l


def count(node, data, l=0):
    return count(node.next, data, l + (node.data == data)) if node else l
