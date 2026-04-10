arr=[1,1,3,3,3,2,2,4,4,5,5,7,7,7,8,8,7,6,5,4,3,2,1]
n=len(arr)
def countingsort(arr,n):
     mx=max(arr)
     freq=[0]*(mx+1)
     for i in arr:
         freq[i]+=1
     arr.clear()
     for i in range(mx+1):
         while freq[i]>0:
              arr.append(i)
              freq[i]-=1
countingsort(arr,n)
print(arr)