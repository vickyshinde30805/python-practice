from sortedcontainers import SortedList

class Fenwick:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def update(self, i, val):
        while i <= self.n:
            self.bit[i] = max(self.bit[i], val)
            i += i & -i

    def query(self, i):
        ans = 0
        while i > 0:
            ans = max(ans, self.bit[i])
            i -= i & -i
        return ans


class Solution:
    def getResults(self, queries):
        mx = 0
        obstacles = set()

        for q in queries:
            mx = max(mx, q[1])
            if q[0] == 1:
                obstacles.add(q[1])

        sl = SortedList([0, mx + 1])

        for x in obstacles:
            sl.add(x)

        bit = Fenwick(mx + 2)

        for i in range(1, len(sl)):
            bit.update(sl[i], sl[i] - sl[i - 1])

        result = []

        for q in reversed(queries):
            if q[0] == 2:
                x, sz = q[1], q[2]

                idx = sl.bisect_right(x)
                prev = sl[idx - 1]

                best = bit.query(prev)

                if idx < len(sl):
                    best = max(best, x - prev)

                result.append(best >= sz)

            else:
                x = q[1]

                idx = sl.index(x)

                left = sl[idx - 1]
                right = sl[idx + 1]

                sl.remove(x)

                bit.update(right, right - left)

        return result[::-1]


# Driver Code
queries1 = [[1,2],[2,3,3],[2,3,1],[2,2,2]]
queries2 = [[1,7],[2,7,6],[1,2],[2,7,5],[2,7,6]]

obj = Solution()

print(obj.getResults(queries1))
print(obj.getResults(queries2))