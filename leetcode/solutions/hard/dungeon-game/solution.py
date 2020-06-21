class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        height, width = len(dungeon) - 1, len(dungeon[0]) - 1
        seen = defaultdict(lambda: (float('inf'), float('inf')))
        queue = [(max(-dungeon[0][0], 0), -dungeon[0][0], [0, 0])]

        while queue:
            min_health, health, (x, y) = heappop(queue)
            health = -health

            if x == height and y == width:
                return max(min_health + 1, 1)

            for x_step, y_step in (1, 0), (0, 1):
                xx, yy = x + x_step, y + y_step

                if 0 <= xx <= height and 0 <= yy <= width:
                    new_health = health + dungeon[xx][yy]
                    new_min_health = -min(-min_health, new_health)

                    if seen[xx, yy] > (-new_health, new_min_health):
                        seen[xx, yy] = (-new_health, new_min_health)
                        heappush(queue, (new_min_health, -new_health, [xx, yy]))
