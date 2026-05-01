def reverse(x: int) -> int:
    # Store sign
    sign = -1 if x < 0 else 1
    
    # Make number positive
    x = abs(x)
    
    # Reverse digits
    rev = 0
    while x != 0:
        digit = x % 10
        rev = rev * 10 + digit
        x //= 10
    
    # Restore sign
    rev *= sign
    
    # Check 32-bit integer range
    if rev < -2**31 or rev > 2**31 - 1:
        return 0
    
    return rev


# Input from user
x = int(input("Enter number: "))

# Output result
print("Reversed number:", reverse(x))