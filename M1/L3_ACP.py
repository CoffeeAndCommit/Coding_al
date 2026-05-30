# Assignment: Congratulations message
# Create a program using string operations

# Variables
name = "Alex"
achievement = "winning the coding competition"

# 1. String Concatenation (+)
message = "Congratulations, " + name + "! " + "You did an amazing job " + achievement + "."

# 2. String Repetition (*)
cheer = "Hip hip hooray! " * 3

# 3. String Methods (upper, lower)
loud_message = message.upper()

# Displaying the results
print("Original Message:")
print(message)
print("\nLoud Message:")
print(loud_message)
print("\nCheer:")
print(cheer)

# 4. Finding string length
message_length = len(message)
print("\nFun fact: The congratulations message has", message_length, "characters!")
