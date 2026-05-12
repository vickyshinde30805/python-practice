def generateParenthesis(n):
    ans = []

    def backtrack(curr, open_count, close_count):
        # If the string is complete
        if len(curr) == 2 * n:
            ans.append(curr)
            return

        # Add opening bracket if possible
        if open_count < n:
            backtrack(curr + "(", open_count + 1, close_count)

        # Add closing bracket only if valid
        if close_count < open_count:
            backtrack(curr + ")", open_count, close_count + 1)

    backtrack("", 0, 0)
    return ans


# Input from user
n = int(input("Enter n: "))

# Generate and print result
result = generateParenthesis(n)

print("Well-formed parentheses combinations:")
for combination in result:
    print(combination)