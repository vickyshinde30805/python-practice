def isPalindrome(x):
    # Negative numbers or numbers ending with 0 (except 0) are not palindrome
    if x < 0 or (x % 10 == 0 and x != 0):
        return False

    reversed_half = 0

    # Reverse half of the number
    while x > reversed_half:
        reversed_half = reversed_half * 10 + x % 10
        x //= 10

    # Check palindrome
    return x == reversed_half or x == reversed_half // 10


# Input from user
x = int(input("Enter a number: "))

# Output result
if isPalindrome(x):
    print("True")
else:
    print("False")