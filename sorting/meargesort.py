arr=[1,3,5,6,7,4,2,8]
n=len(arr)
def merge(arr,l,mid,r):
    A,B=arr[l:mid+1],arr[mid+1:r+1]
    n,m=len(A),len(B)

    i,j,k=0,0,l
    while i<n or j<m:
        if j==m:
            arr[k]=A[i]
            i+=1
            k+=1
        elif i==n:
            arr[k]=B[j]
            j+=1
            k+=1
        elif A[i]<=B[j]:
            arr[k]=A[i]
            i+=1
            k+=1
        else:
            arr[k]=B[j]
            j+=1
            k+=1
def mergesort(arr,l,r):
    if l<r:
        mid=(l+r)//2
        mergesort(arr,l,mid)
        mergesort(arr,mid+1,r)
        merge(arr,l,mid,r)
mergesort(arr,0,n)
print(arr)