# Assignment: Circumference
# Write a program to create a python function to calculate the circumference of a circle

def calculate_circumference(radius):
    """
    Function to calculate the circumference of a circle.
    Formula: 2 * pi * radius
    """
    import math
    return 2 * math.pi * radius

# Take radius input from the user
try:
    radius = float(input("Enter the radius of the circle: "))
    
    if radius < 0:
        print("Radius cannot be negative!")
    else:
        # Call the function and print the result
        circumference = calculate_circumference(radius)
        print(f"The circumference of the circle is: {circumference:.2f}")

except ValueError:
    print("Invalid input! Please enter a valid number for the radius.")
