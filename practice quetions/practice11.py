# Beginner-friendly DFS / BFS approach (works in LeetCode & VS Code)

from typing import List

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        visited = set()   # To avoid infinite loops
        stack = [start]   # DFS stack
        
        while stack:
            i = stack.pop()
            
            # If out of bounds or already visited, skip
            if i < 0 or i >= n or i in visited:
                continue
            
            # If we found 0
            if arr[i] == 0:
                return True
            
            # Mark visited
            visited.add(i)
            
            # Jump forward and backward
            stack.append(i + arr[i])
            stack.append(i - arr[i])
        
        return False


# Example usage:
arr = [4,2,3,0,3,1,2]
start = 5

sol = Solution()
print(sol.canReach(arr, start))   # Output: True