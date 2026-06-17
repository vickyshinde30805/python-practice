class Solution:
    def processStr(self, s: str, k: int) -> str:
        lengths = []
        curr_len = 0

        # Find length after each operation
        for ch in s:
            if ch.isalpha():
                curr_len += 1

            elif ch == "#":
                curr_len *= 2

            elif ch == "*":
                if curr_len > 0:
                    curr_len -= 1

            # '%' does not change length

            lengths.append(curr_len)

        # Check if k is valid (0-based indexing)
        if k < 0 or k >= curr_len:
            return "."

        # Work backwards
        for i in range(len(s) - 1, -1, -1):
            ch = s[i]

            if ch.isalpha():
                if k == lengths[i] - 1:
                    return ch

            elif ch == "#":
                half = lengths[i] // 2
                k %= half

            elif ch == "%":
                k = lengths[i] - 1 - k

        return "."
sol = Solution()

print(sol.processStr("ab#", 0))  # a
print(sol.processStr("ab#", 1))  # b
print(sol.processStr("ab#", 2))  # a
print(sol.processStr("ab#", 3))  # b