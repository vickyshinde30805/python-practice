arr=[2,1,5,3,6,7,8,4]
n=len(arr)
def partition(arr,l,r):
    key=arr[r]
    start=l
    for i in range(l,r+1):
        if arr[i]<=key:
            arr[i],arr[start]=arr[start],arr[i]
            start+=1
    return start-1
def quiksort(arr,l,r):
    if l<r:
         pi=partition(arr,l,r)
         quiksort(arr,l,pi-1)
         quiksort(arr,pi+1,r)
quiksort(arr,0,n-1)
print(arr)