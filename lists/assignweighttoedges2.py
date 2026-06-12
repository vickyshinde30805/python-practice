from collections import defaultdict

MOD = 10**9 + 7

def assignEdgeWeights(edges):
    n = len(edges) + 1

    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    leaf_depth = None

    def dfs(node, parent, depth):
        nonlocal leaf_depth

        if node != 1 and len(graph[node]) == 1:
            if leaf_depth is None:
                leaf_depth = depth
            return

        for nei in graph[node]:
            if nei != parent:
                dfs(nei, node, depth + 1)

    dfs(1, -1, 0)

    return pow(2, leaf_depth - 1, MOD)

edges = [[1,2],[1,3],[3,4],[3,5]]
print(assignEdgeWeights(edges))