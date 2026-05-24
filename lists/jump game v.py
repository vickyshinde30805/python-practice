from typing import List


class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:

        n = len(arr)

        # dp[i] stores maximum jumps starting from index i
        dp = [-1] * n

        def dfs(i):

            # if already calculated
            if dp[i] != -1:
                return dp[i]

            ans = 1

            # move right
            for j in range(i + 1, min(n, i + d + 1)):

                # stop if greater or equal element found
                if arr[j] >= arr[i]:
                    break

                ans = max(ans, 1 + dfs(j))

            # move left
            for j in range(i - 1, max(-1, i - d - 1), -1):

                # stop if greater or equal element found
                if arr[j] >= arr[i]:
                    break

                ans = max(ans, 1 + dfs(j))

            dp[i] = ans
            return ans

        result = 0

        for i in range(n):
            result = max(result, dfs(i))

        return result


# Driver Code for VS Code
arr = [6, 4, 14, 6, 8, 13, 9, 7, 10, 6, 12]
d = 2

obj = Solution()

print("Maximum indices visited:", obj.maxJumps(arr, d))