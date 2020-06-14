from collections import defaultdict
from typing import List, Dict, Tuple
from heapq import heappush, heappop

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph: Dict[int, List[Tuple[int, int]]] = defaultdict(list)
        for node, dst_node, price in flights:
            graph[node].append((dst_node, price))

        queue: List[Tuple[int, List[int]]] = [(0, [src])]

        while queue:
            price, path = heappop(queue)

            if path[-1] == dst:
                return price
            elif len(path) - 1 > k:
                continue

            for dst_node, path_price in graph[path[-1]]:
                heappush(queue, (price + path_price, [*path, dst_node]))

        return -1