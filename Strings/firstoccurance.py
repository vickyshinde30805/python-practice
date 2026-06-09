haystack = "hello"
needle = "ll"

n = len(haystack)
m = len(needle)

for i in range(n - m + 1):
    if haystack[i:i+m] == needle:
        print(i)
        break
else:
    print(-1)