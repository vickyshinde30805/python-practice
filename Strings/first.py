from heapq import heappush, heappop

class SparseTable:
    def __init__(self, nums):
        n = len(nums)

        self.log = [0] * (n + 1)
        for i in range(2, n + 1):
            self.log[i] = self.log[i // 2] + 1

        K = self.log[n] + 1

        self.mx = [[0] * K for _ in range(n)]
        self.mn = [[0] * K for _ in range(n)]

        for i in range(n):
            self.mx[i][0] = nums[i]
            self.mn[i][0] = nums[i]

        j = 1
        while (1 << j) <= n:
            half = 1 << (j - 1)

            for i in range(n - (1 << j) + 1):
                self.mx[i][j] = max(
                    self.mx[i][j - 1],
                    self.mx[i + half][j - 1]
                )

                self.mn[i][j] = min(
                    self.mn[i][j - 1],
                    self.mn[i + half][j - 1]
                )

            j += 1

    def get_max(self, l, r):
        k = self.log[r - l + 1]
        return max(
            self.mx[l][k],
            self.mx[r - (1 << k) + 1][k]
        )

    def get_min(self, l, r):
        k = self.log[r - l + 1]
        return min(
            self.mn[l][k],
            self.mn[r - (1 << k) + 1][k]
        )


def maxTotalValue(nums, k):
    n = len(nums)
    st = SparseTable(nums)

    heap = []

    for l in range(n):
        value = st.get_max(l, n - 1) - st.get_min(l, n - 1)
        heappush(heap, (-value, l, n - 1))

    ans = 0

    for _ in range(k):
        value, l, r = heappop(heap)
        ans += -value

        if r > l:
            new_value = st.get_max(l, r - 1) - st.get_min(l, r - 1)
            heappush(heap, (-new_value, l, r - 1))

    return ans


# Input
nums = list(map(int, input("Enter array: ").split()))
k = int(input("Enter k: "))

# Output
print("Maximum Total Value =", maxTotalValue(nums, k))