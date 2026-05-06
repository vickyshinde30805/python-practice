count=0
n=int(input("Enter the value of n : "))
while n!=1:
    print(n,end=" -> ")
    if n%2==0:
        n=n//2
    else:
        n=3*n+1
    count+=1
print(n)
print("\nTotal steps : ",count)