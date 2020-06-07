class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        ways = [[0] * (amount + 1) for _ in range(len(coins) + 1)]
        ways[0][0] = 1

        for i in range(1, len(coins) + 1):
            ways[i][0] = 1

            for j in range(1, amount + 1):
                ways[i][j] = ways[i - 1][j] + (0 if j < coins[i - 1] else ways[i][j - coins[i - 1]])

        return ways[-1][amount]