from typing import List

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        s1 = set()
        s2 = set()
        ans = []

        for i in range(len(A)):
            s1.add(A[i])
            s2.add(B[i])

            count = 0

            for num in s1:
                if num in s2:
                    count += 1

            ans.append(count)

        return ans


# Example usage
obj = Solution()

A = [1, 3, 2, 4]
B = [3, 1, 2, 4]

print(obj.findThePrefixCommonArray(A, B))