def product_list(numbers):
    product = 1
    for num in numbers:
        product *= num
    return product

numbers = [1, 2, 3, 4]
print("Product:", product_list(numbers))