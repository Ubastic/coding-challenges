class DynamicConnectivity:
    def __init__(self, n):
        self.connects = {i: set() for i in range(n)}

    def connected(self, p, q):
        visited = {p}
        queue = [p]

        while queue:
            v = queue.pop()
            connections = self.connects[v]

            if q in connections:
                return True

            queue.extend({*connections} - visited)
            visited.update(connections)

        return False

    def union(self, p, q):
        self.connects[p].add(q)
        self.connects[q].add(p)