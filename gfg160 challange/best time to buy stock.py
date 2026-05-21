class Solution:
    def maximumProfit(self, prices):

        profit = 0

        for i in range(1, len(prices)):

            if prices[i] > prices[i - 1]:

                profit += prices[i] - prices[i - 1]

        return profit


# Driver Code
prices = [100, 180, 260, 310, 40, 535, 695]

obj = Solution()

print(obj.maximumProfit(prices))