# Assignment: Square it Out!
# Create a list of square values of numbers between specified ranges by the user,
# and then separate the odd and even values.

try:
    # Take range inputs from the user
    start = int(input("Enter the starting number of the range: "))
    end = int(input("Enter the ending number of the range: "))
    
    # Generate the list of square values for the range (inclusive)
    squares = [num ** 2 for num in range(start, end + 1)]
    print(f"\nAll square values: {squares}")
    
    # Separate the even and odd squares
    even_squares = [sq for sq in squares if sq % 2 == 0]
    odd_squares = [sq for sq in squares if sq % 2 != 0]
    
    # Display the separated lists
    print(f"Even square values: {even_squares}")
    print(f"Odd square values: {odd_squares}")

except ValueError:
    print("Invalid input! Please enter valid integers for the range.")
