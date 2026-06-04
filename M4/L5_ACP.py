# List Comprehension Examples

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Squares of all numbers
squares = [x ** 2 for x in numbers]
print("Squares:", squares)

# Even numbers
evens = [x for x in numbers if x % 2 == 0]
print("Even Numbers:", evens)

# Odd numbers
odds = [x for x in numbers if x % 2 != 0]
print("Odd Numbers:", odds)

# Numbers greater than 5
greater_than_5 = [x for x in numbers if x > 5]
print("Greater than 5:", greater_than_5)

# Convert words to uppercase
words = ["python", "java", "c++", "javascript"]
uppercase_words = [word.upper() for word in words]
print("Uppercase Words:", uppercase_words)

# Length of each word
lengths = [len(word) for word in words]
print("Word Lengths:", lengths)