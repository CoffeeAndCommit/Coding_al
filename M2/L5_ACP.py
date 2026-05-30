# Assignment: Mirrored Triangle
# Write a program to make a mirrored right-angled triangle

# Take input from the user
rows = int(input("Enter the number of rows: "))

print("Mirrored Right-Angled Triangle:")

# Outer loop to handle the number of rows
for i in range(1, rows + 1):
    
    # Inner loop to print spaces
    for j in range(1, rows - i + 1):
        print(end=" ")
        
    # Inner loop to print stars
    for j in range(1, i + 1):
        print("*", end="")
        
    # Move to the next line after each row
    print()
