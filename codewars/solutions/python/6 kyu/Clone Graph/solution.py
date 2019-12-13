
def clone_graph(node, cache=None):
    if isinstance(node, GraphNode):
        cache = cache or {}
        if id(node) in cache:
            return cache[id(node)]

        n = cache[id(node)] = GraphNode(node.val)
        n.neighbors = [clone_graph(nn, cache) for nn in node.neighbors]

        return n