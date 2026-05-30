# Assignment: Check Age
# Write a program to check if the age entered by the user is between 10 to 20 years

# Take age input from the user
try:
    age = int(input("Enter your age: "))

    # Check if the age is between 10 and 20
    if age >= 10 and age <= 20:
        print("Your age is between 10 and 20 years.")
    else:
        print("Your age is NOT between 10 and 20 years.")

except ValueError:
    print("Invalid input! Please enter a number for your age.")
