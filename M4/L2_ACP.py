# Assignment: Tuple Product
# Write a Python program to calculate the product, multiplying all the numbers of the given tuple.

def calculate_product(tup):
    # Initialize the product to 1
    product = 1
    for num in tup:
        product *= num
    return product

# Test the function with a tuple
test_tuple = (4, 3, 2, 2, -1, 18)
print("The original tuple is:", test_tuple)

result = calculate_product(test_tuple)
print("Product of the tuple elements is:", result)

# Test with another tuple
test_tuple_2 = (1, 2, 3, 4, 5)
print("\nThe original tuple is:", test_tuple_2)
print("Product of the tuple elements is:", calculate_product(test_tuple_2))
