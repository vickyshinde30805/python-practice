def hammingWeight(n: int) -> int:
    count = 0
    while n:
        n = n & (n - 1)   # remove lowest set bit
        count += 1
    return count


# --------- MAIN PROGRAM ----------
if __name__ == "__main__":
    n = int(input("Enter a number: "))
    result = hammingWeight(n)
    print("Number of 1 bits:", result)