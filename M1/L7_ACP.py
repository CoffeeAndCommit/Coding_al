# Assignment: ASCII Value Checker
# This program reveals the numeric ASCII code behind a character.

# Take a single character as input from the user
character = input("Enter a letter, digit, or symbol: ")

# Ensure the user entered exactly one character
if len(character) == 1:
    # Use the ord() function to find the ASCII value
    ascii_value = ord(character)
    print("The ASCII value of '" + character + "' is:", ascii_value)
else:
    print("Please enter exactly one character.")
