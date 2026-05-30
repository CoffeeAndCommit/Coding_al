# Assignment: Power calculator
# Write a program to calculate the n-th power of a given number

# Take base and exponent as input from the user
base = int(input("Enter the base number: "))
power = int(input("Enter the power (exponent): "))

result = 1

# Since this lesson focuses on loops, let's calculate the power using a for loop!
for i in range(power):
    result = result * base

# You could also simply use: result = base ** power

print("\nResult:")
print(f"{base} raised to the power of {power} is: {result}")
