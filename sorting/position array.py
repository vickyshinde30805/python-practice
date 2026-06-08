class Solution:
    def pivotArray(self, nums, pivot):
        left, mid, right = [], [], []

        for num in nums:
            if num < pivot:
                left.append(num)
            elif num == pivot:
                mid.append(num)
            else:
                right.append(num)

        return left + mid + right


# Test
nums = [9, 12, 5, 10, 14, 3, 10]
pivot = 10

sol = Solution()
print(sol.pivotArray(nums, pivot))