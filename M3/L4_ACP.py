# Assignment: Age Counter
# Write a program to check if the age entered by the user is correct or not.
# If there is some error in the value of age entered, handle it.
# Also, check whether the age entered by the user is even or odd.

def validate_age(age):
    # Check if the age is in a realistic range
    if age < 0:
        raise ValueError("Age cannot be negative.")
    if age > 130:
        raise ValueError("Age is unrealistic. Please enter an age between 0 and 130.")
    return age

try:
    user_input = input("Enter your age: ")
    # Convert input to integer
    age = int(user_input)
    
    # Validate if age is correct/realistic
    valid_age = validate_age(age)
    
    # Check even or odd
    if valid_age % 2 == 0:
        print(f"The age {valid_age} is Even.")
    else:
        print(f"The age {valid_age} is Odd.")

except ValueError as ex:
    # Handle non-numeric input or validation failure
    if "invalid literal" in str(ex):
        print("Invalid input! Please enter a valid integer for age.")
    else:
        print(f"Error: {ex}")
