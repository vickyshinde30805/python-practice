from typing import List

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:

        # Find the maximum cost
        max_cost = max(costs)

        # Create frequency array for counting sort
        freq = [0] * (max_cost + 1)

        # Count occurrences of each cost
        for cost in costs:
            freq[cost] += 1

        # Number of ice creams bought
        bars = 0

        # Process costs from smallest to largest
        for cost in range(1, max_cost + 1):

            # Skip if no ice cream has this cost
            if freq[cost] == 0:
                continue

            # Maximum ice creams we can buy at this cost
            can_buy = min(freq[cost], coins // cost)

            # Add to answer
            bars += can_buy

            # Deduct spent coins
            coins -= can_buy * cost

        return bars


# Example usage in VS Code
costs = [1, 3, 2, 4, 1]
coins = 7

obj = Solution()
print(obj.maxIceCream(costs, coins))