arr=[1,3,5,6,7,9,3,245]
n=len(arr)
def linearsearch(arr,target):
    for i in range(n):
        if arr[i]==target:
            return i
    return -1

print(linearsearch(arr,6))