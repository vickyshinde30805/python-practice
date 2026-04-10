arr=[2,4,5,6,7,8,3,1]
n=len(arr)
def selectionsort(arr,n):
    for i in range(n):
        idx=i
        for j in range(i+1,n):
            if arr[j]<arr[idx]:
                idx=j
            arr[idx],arr[i]=arr[i],arr[idx]
selectionsort(arr,n)
print(arr)