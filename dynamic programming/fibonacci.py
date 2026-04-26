class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]


# 🔽 Main function (for VS Code)
if __name__ == "__main__":
    n = int(input("Enter value of n: "))
    sol = Solution()
    result = sol.fib(n)
    print("Fibonacci number is:", result)