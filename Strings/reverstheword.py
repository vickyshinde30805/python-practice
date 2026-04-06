s="The sky is blue"
def reverseword(s):
    return" ".join(s.strip().split()[::-1])
print(reverseword(s))