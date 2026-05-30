# Assignment: Total Digits
# Write a program to calculate how many total digits are in a number entered by the user

# Take input from the user
num = int(input("Enter a number: "))

# Use abs() to safely handle negative numbers
temp = abs(num)
count = 0

# If the user simply enters 0, it has 1 digit
if temp == 0:
    count = 1
else:
    # Use a while loop to repeatedly chop off the last digit
    while temp > 0:
        count += 1
        temp //= 10  # Integer division to remove the last digit

print(f"\nThe total number of digits in {num} is: {count}")
