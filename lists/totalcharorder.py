words = ["abcd", "def", "xyz"]
weights = [5,3,12,14,1,2,3,2,10,6,6,9,7,8,7,10,8,9,6,9,9,8,3,7,7,2]

# letter -> weight mapping
value = {}
for i in range(26):
    value[chr(97 + i)] = weights[i]

ans = ""

for word in words:
    total = 0

    for ch in word:
        total += value[ch]

    mod = total % 26

    # reverse mapping: 0->z, 1->y, ..., 25->a
    ans += chr(ord('z') - mod)

print(ans)