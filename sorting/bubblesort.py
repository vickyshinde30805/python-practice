arr=[1,4,3,5,7,6,8,2]
n=len(arr)
def bubblesort(arr,n):
    for i in range(n):
         isSorted=True
         for j in range(n-i-1):
               if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                isSorted=False
         if isSorted:
            break
bubblesort(arr,n)
print(arr)