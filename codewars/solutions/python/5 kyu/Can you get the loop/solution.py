def loop_size(node):
    nodes = []
    while node not in nodes:
        nodes.append(node)
        node = node.next
    
    return len(nodes) - nodes.index(node)
    