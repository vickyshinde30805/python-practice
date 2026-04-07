def sumofnum(n):
    if n==0:
        return 0
    return sumofnum(n-1)+n
print(sumofnum(5))
    
          