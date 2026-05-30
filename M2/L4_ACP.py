# Assignment: Binary conversion
# Write a program to convert a decimal number into a binary number

# Take a decimal number as input from the user
decimal_num = int(input("Enter a decimal number: "))

# Store the original number to display it later
original_num = decimal_num

# Initialize an empty string to store the binary digits
binary_str = ""

# Handle the edge case if the user enters 0
if decimal_num == 0:
    binary_str = "0"
else:
    # Use a while loop to repeatedly divide by 2 and get the remainders
    while decimal_num > 0:
        remainder = decimal_num % 2
        
        # Prepend the remainder to our binary string
        binary_str = str(remainder) + binary_str
        
        # Divide by 2 to move to the next digit
        decimal_num = decimal_num // 2

# Display the result
print(f"The binary representation of {original_num} is: {binary_str}")
