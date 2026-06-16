class Solution:
    def processStr(self, s: str) -> str:
        res = []

        for ch in s:
            if ch.isalpha():
                res.append(ch)
            elif ch == '#':
                res *= 2
            elif ch == '%':
                res.reverse()
            elif ch == '*' and res:
                res.pop()

        return ''.join(res)


# Test
sol = Solution()
print(sol.processStr("ab#%"))  # baba