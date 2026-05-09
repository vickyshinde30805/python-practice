from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        n = len(nums)

        ans = set()

        # Brute Force - O(n^4)

        for i in range(n):

            for j in range(i + 1, n):

                for k in range(j + 1, n):

                    for l in range(k + 1, n):

                        total = nums[i] + nums[j] + nums[k] + nums[l]

                        if total == target:

                            temp = sorted([
                                nums[i],
                                nums[j],
                                nums[k],
                                nums[l]
                            ])

                            ans.add(tuple(temp))

        return [list(x) for x in ans]


# --------------------------------
# Driver Code for VS Code
# --------------------------------

nums = [1, 0, -1, 0, -2, 2]
target = 0

obj = Solution()

result = obj.fourSum(nums, target)

print("Quadruplets are:")

for quad in result:
    print(quad)