from bisect import bisect_left

class Fenwick:
    def __init__(self, n):
        self.bit = [0] * (n + 1)

    def update(self, i, val):
        while i < len(self.bit):
            self.bit[i] += val
            i += i & -i

    def query(self, i):
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s


class Solution:
    def countMajoritySubarrays(self, nums, target):
        prefix = [0]
        s = 0

        # Convert array: target -> +1, others -> -1
        for x in nums:
            if x == target:
                s += 1
            else:
                s -= 1
            prefix.append(s)

        # Coordinate Compression
        values = sorted(set(prefix))

        bit = Fenwick(len(values))
        ans = 0

        # Count valid subarrays
        for p in prefix:
            idx = bisect_left(values, p) + 1
            ans += bit.query(idx - 1)
            bit.update(idx, 1)

        return ans


# ---------------- Driver Code ----------------
if __name__ == "__main__":
    nums = [1, 2, 2, 3]
    target = 2

    obj = Solution()
    print(obj.countMajoritySubarrays(nums, target))