def count_up_to(n):
    i = 1
    while i <= n:
        yield i   # pause and return value
        i += 1

# Using the generator
for num in count_up_to(5):
    print(num)