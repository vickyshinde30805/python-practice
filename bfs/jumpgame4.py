from collections import defaultdict, deque

def minJumps(arr):
    n = len(arr)

    # If already at last index
    if n == 1:
        return 0

    # Store indices of same values
    mp = defaultdict(list)
    for i, num in enumerate(arr):
        mp[num].append(i)

    # BFS
    q = deque([0])
    visited = [False] * n
    visited[0] = True

    steps = 0

    while q:
        for _ in range(len(q)):
            curr = q.popleft()

            # Reached last index
            if curr == n - 1:
                return steps

            # Jump to i + 1
            if curr + 1 < n and not visited[curr + 1]:
                visited[curr + 1] = True
                q.append(curr + 1)

            # Jump to i - 1
            if curr - 1 >= 0 and not visited[curr - 1]:
                visited[curr - 1] = True
                q.append(curr - 1)

            # Jump to same value positions
            for nxt in mp[arr[curr]]:
                if not visited[nxt]:
                    visited[nxt] = True
                    q.append(nxt)

            # Clear processed value group
            mp[arr[curr]].clear()

        steps += 1

    return -1


# Driver Code
arr = list(map(int, input("Enter array elements: ").split()))

result = minJumps(arr)

print("Minimum jumps to reach last index:", result)