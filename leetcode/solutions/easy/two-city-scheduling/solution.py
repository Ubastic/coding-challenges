class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs = sorted(costs, key=lambda cost: cost[0] - cost[1])
        return sum(c for c, _ in costs[:len(costs) // 2]) + sum(c for _, c in costs[len(costs) // 2:])
