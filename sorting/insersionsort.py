arr=[3,2,1,4,5,8,7,6]
n=len(arr)
def insersionsort(arr,n):
     for i in range (1,n):
         key=arr[i]
         j=i-1
         while j>=0:
              if arr[j]<key:
                    break
              arr[j+1]=arr[j]
              j-=1
         arr[j+1]=key

insersionsort(arr,n)
print(arr)

    