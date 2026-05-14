# Good Array / Good List Problem for VS Code
# Checks if array becomes [1,2,3,...,n-1,n-1]

class Solution:
    def isGood(self, nums):
        # Sort the list
        nums.sort()
        n = len(nums)

        # Last two elements must be same
        if nums[n - 1] != nums[n - 2]:
            return False

        # Last element should be n-1
        if nums[n - 1] != n - 1:
            return False

        # First elements should be 1 to n-1
        for i in range(n - 1):
            if nums[i] != i + 1:
                return False

        return True


# Driver Code for VS Code
nums = list(map(int, input("Enter list elements: ").split()))

sol = Solution()

if sol.isGood(nums):
    print("True")
else:
    print("False")