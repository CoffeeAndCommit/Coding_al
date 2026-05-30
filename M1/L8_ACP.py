# Assignment: Number swap
# Create a program to swap three numbers

# Take three numbers as input from the user
a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))
c = int(input("Enter third number (c): "))

print("\nOriginal numbers:")
print("a =", a)
print("b =", b)
print("c =", c)

# Swapping the three numbers using Python's multiple assignment feature
# Let's do a cyclic swap: a gets the value of c, b gets a, c gets b
a, b, c = c, a, b

# Alternatively, you could use a temporary variable:
# temp = a
# a = c
# c = b
# b = temp

print("\nAfter swapping:")
print("a =", a)
print("b =", b)
print("c =", c)
