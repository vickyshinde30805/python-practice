from typing import List

class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:

        n = len(grid)
        m = len(grid[0])

        layers = min(n, m) // 2

        for layer in range(layers):

            col_start, col_end = layer, m - layer - 1
            row_start, row_end = layer, n - layer - 1

            ans = []

            # -------------------------
            # Extract layer
            # -------------------------

            # Left column
            for i in range(row_start, row_end + 1):
                ans.append(grid[i][col_start])

            # Bottom row
            for i in range(col_start + 1, col_end + 1):
                ans.append(grid[row_end][i])

            # Right column
            for i in range(row_end - 1, row_start - 1, -1):
                ans.append(grid[i][col_end])

            # Top row
            for i in range(col_end - 1, col_start, -1):
                ans.append(grid[row_start][i])

            # -------------------------
            # Rotate
            # -------------------------
            rotate = k % len(ans)

            ans = ans[-rotate:] + ans[:-rotate]

            # -------------------------
            # Put back rotated values
            # -------------------------
            idx = 0

            # Left column
            for i in range(row_start, row_end + 1):
                grid[i][col_start] = ans[idx]
                idx += 1

            # Bottom row
            for i in range(col_start + 1, col_end + 1):
                grid[row_end][i] = ans[idx]
                idx += 1

            # Right column
            for i in range(row_end - 1, row_start - 1, -1):
                grid[i][col_end] = ans[idx]
                idx += 1

            # Top row
            for i in range(col_end - 1, col_start, -1):
                grid[row_start][i] = ans[idx]
                idx += 1

        return grid


# --------------------------------
# Driver Code for VS Code
# --------------------------------

grid = [
    [40, 10],
    [30, 20]
]

k = 1

obj = Solution()

result = obj.rotateGrid(grid, k)

print("Rotated Grid:")

for row in result:
    print(row)