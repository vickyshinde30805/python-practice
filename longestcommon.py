class Solution:
    def minCostClimbingStairs(self, cost):
        
        n = len(cost)

        # dp[i] = minimum cost to reach step i
        dp = [0] * (n + 1)

        # Fill dp array
        for i in range(2, n + 1):
            one_step = dp[i - 1] + cost[i - 1]
            two_steps = dp[i - 2] + cost[i - 2]

            dp[i] = min(one_step, two_steps)

        return dp[n]


# VS Code Input
cost = list(map(int, input("Enter stair costs separated by space: ").split()))

solution = Solution()

print("Minimum Cost:", solution.minCostClimbingStairs(cost))