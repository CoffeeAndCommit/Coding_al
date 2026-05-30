# Assignment: Checking Alphabets
# Create a program to check if the given character is an alphabet or not

# Taking a single character as input
char = input("Enter a character: ")

# Using logical operators (and, or) to check if the character is an alphabet
# We check if it falls in the range of lowercase (a-z) or uppercase (A-Z)
if (char >= 'a' and char <= 'z') or (char >= 'A' and char <= 'Z'):
    print(char, "is an alphabet.")
else:
    print(char, "is not an alphabet.")
