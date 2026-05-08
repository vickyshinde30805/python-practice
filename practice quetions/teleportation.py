from collections import defaultdict, deque


class Solution:
    def minJumps(self, nums):
        n = len(nums)

        # If already at destination
        if n == 1:
            return 0

        # -----------------------------------
        # STEP 1: Smallest Prime Factor (SPF)
        # -----------------------------------
        max_num = max(nums)
        spf = list(range(max_num + 1))

        for i in range(2, int(max_num ** 0.5) + 1):
            if spf[i] == i:  # i is prime
                for j in range(i * i, max_num + 1, i):
                    if spf[j] == j:
                        spf[j] = i

        # -----------------------------------
        # STEP 2: Prime Factor -> Indices Map
        # -----------------------------------
        mp = defaultdict(list)

        for index, num in enumerate(nums):
            temp = num
            used_factor = set()

            while temp > 1:
                prime_factor = spf[temp]

                if prime_factor not in used_factor:
                    mp[prime_factor].append(index)
                    used_factor.add(prime_factor)

                while temp % prime_factor == 0:
                    temp //= prime_factor

        # -----------------------------------
        # STEP 3: BFS
        # -----------------------------------
        que = deque([0])
        visited = [False] * n
        visited[0] = True

        step = 0
        used_prime = set()

        while que:
            size = len(que)

            while size > 0:
                i = que.popleft()

                # Reached end
                if i == n - 1:
                    return step

                # Move Left
                if i - 1 >= 0 and not visited[i - 1]:
                    visited[i - 1] = True
                    que.append(i - 1)

                # Move Right
                if i + 1 < n and not visited[i + 1]:
                    visited[i + 1] = True
                    que.append(i + 1)

                # Prime Teleport
                current_value = nums[i]

                # If current value itself is prime
                if current_value > 1 and spf[current_value] == current_value:

                    # Process each prime only once
                    if current_value not in used_prime:
                        used_prime.add(current_value)

                        for j in mp[current_value]:
                            if not visited[j]:
                                visited[j] = True
                                que.append(j)

                size -= 1

            step += 1

        return -1


# -----------------------------------
# VS CODE TESTING
# -----------------------------------
if __name__ == "__main__":
    sol = Solution()

    # Test Cases
    nums1 = [1, 2, 4, 6]
    nums2 = [2, 3, 4, 7, 9]
    nums3 = [4, 6, 5, 8]

    print("Output 1:", sol.minJumps(nums1))  # Expected 2
    print("Output 2:", sol.minJumps(nums2))  # Expected 2
    print("Output 3:", sol.minJumps(nums3))  # Expected 3