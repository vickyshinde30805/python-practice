class Solution:
    def assignEdgeWeights(self, edges):
        MOD = 10**9 + 7
        n = len(edges) + 1

        g = [[] for _ in range(n + 1)]

        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        def dfs(node, parent):
            depth = 0
            for nei in g[node]:
                if nei != parent:
                    depth = max(depth, 1 + dfs(nei, node))
            return depth

        d = dfs(1, 0)

        return 0 if d == 0 else pow(2, d - 1, MOD)


edges = [[1, 2], [2, 3]]
print(Solution().assignEdgeWeights(edges))