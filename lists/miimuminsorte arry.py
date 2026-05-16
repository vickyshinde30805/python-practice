class Solution:
    def findMin(self, nums):
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            # Handle duplicates
            if nums[mid] == nums[right]:
                right -= 1
            # Minimum is in right half
            elif nums[mid] > nums[right]:
                left = mid + 1
            # Minimum is in left half including mid
            else:
                right = mid

        return nums[left]


# VS Code Input/Output
nums = list(map(int, input("Enter array elements: ").split()))

sol = Solution()
print("Minimum element is:", sol.findMin(nums))