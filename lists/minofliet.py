class Solution:
    def findMin(self, nums):
        left = 0
        right = len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            # Minimum is in right half
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                # Minimum is in left half including mid
                right = mid
        
        return nums[left]


# VS Code Input/Output Example
nums = list(map(int, input("Enter array elements: ").split()))

sol = Solution()
print("Minimum element is:", sol.findMin(nums))