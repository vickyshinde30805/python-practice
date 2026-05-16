# Your brute force permutation approach is failing for large test cases
# and may return wrong due to inefficiency.
# Use the OPTIMAL O(n) approach below.

class Solution:
    def nextPermutation(self, arr):
        n = len(arr)

        # Step 1: Find breakpoint (first smaller from right)
        index = -1
        for i in range(n - 2, -1, -1):
            if arr[i] < arr[i + 1]:
                index = i
                break

        # Step 2: If no breakpoint, reverse whole array
        if index == -1:
            arr.reverse()
            return arr

        # Step 3: Find next greater element from right
        for i in range(n - 1, index, -1):
            if arr[i] > arr[index]:
                arr[i], arr[index] = arr[index], arr[i]
                break

        # Step 4: Reverse suffix (right side)
        left = index + 1
        right = n - 1

        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

        return arr


# Example:
arr = [1, 2, 3, 6, 5, 4]

sol = Solution()
print(sol.nextPermutation(arr))

# Output:
# [1, 2, 4, 3, 5, 6]