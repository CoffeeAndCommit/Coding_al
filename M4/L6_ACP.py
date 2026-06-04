import random
import string

# Password length
length = 12

# Characters to use
lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
digits = string.digits

# Ensure at least one lowercase, one uppercase, and one digit
password = [
    random.choice(lowercase),
    random.choice(uppercase),
    random.choice(digits)
]

# Fill remaining characters
all_characters = lowercase + uppercase + digits

for i in range(length - 3):
    password.append(random.choice(all_characters))

# Shuffle password
random.shuffle(password)

# Convert list to string
password = "".join(password)

print("Generated Password:", password)