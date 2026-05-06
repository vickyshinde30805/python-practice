import math

def findlog(n):
    if n<=0:
        return -1
    return (math.log(n,3))
print(findlog(800000000))