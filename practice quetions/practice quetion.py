# LeetCode 2770 - Maximum Number of Jumps to Reach the Last Index
# VS Code Ready Version

from typing import List


class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        n = len(nums)

        # dp[i] = maximum number of jumps to reach index i
        dp = [-1] * n
        dp[0] = 0  # Start from index 0

        # Fill DP table
        for i in range(n):
            # Skip if current index is unreachable
            if dp[i] == -1:
                continue

            # Try jumping to all next positions
            for j in range(i + 1, n):
                # Check valid jump condition
                if abs(nums[j] - nums[i]) <= target:
                    dp[j] = max(dp[j], dp[i] + 1)

        return dp[n - 1]


# -------------------------
# Driver Code for VS Code
# -------------------------
if __name__ == "__main__":
    # Input array
    nums = list(map(int, input("Enter array elements separated by space: ").split()))
    
    # Input target
    target = int(input("Enter target: "))

    # Create object
    sol = Solution()

    # Get result
    result = sol.maximumJumps(nums, target)

    # Output result
    print("Maximum jumps to reach last index:", result)