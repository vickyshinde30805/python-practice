def nextGreaterElements(nums):
    n = len(nums)
    stack = []
    ans = [-1] * n

    # Traverse twice for circular array
    for i in range(2 * n):
        while stack and nums[stack[-1]] < nums[i % n]:
            idx = stack.pop()
            ans[idx] = nums[i % n]

        # Push only first pass
        if i < n:
            stack.append(i)

    return ans


# 🔹 Input
nums = list(map(int, input("Enter elements: ").split()))

# 🔹 Function Call
result = nextGreaterElements(nums)

# 🔹 Output
print("Next Greater Elements:", result)