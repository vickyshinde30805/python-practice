"""n=int (input ("Enter the no:"))
if n%2==0:
    print ("even")
else :
    print("odd")"""
#greatest of no
num1=int (input("Enter the no1:"))
num2=int (input("Enter the no2:"))
num3=int (input("Enter the no3:"))

if num1>num2 and num1>num3:
    print("num1 is greatest",num1)
elif num2>num1 and num2>num3:
    print(num2)

else:
    print (num3)