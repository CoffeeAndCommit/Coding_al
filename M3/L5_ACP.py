# Assignment: Trigonometric value
# Write a program to calculate the values of sin, cos, and tan using the math module.

import math

try:
    # Take input from the user in degrees
    angle_degrees = float(input("Enter the angle in degrees: "))
    
    # Convert degrees to radians because math functions expect radians
    angle_radians = math.radians(angle_degrees)
    
    # Calculate sin, cos, and tan values
    sin_val = math.sin(angle_radians)
    cos_val = math.cos(angle_radians)
    tan_val = math.tan(angle_radians)
    
    # Display the results
    print(f"\nTrigonometric values for {angle_degrees}°:")
    print(f"Sin({angle_degrees}) = {sin_val:.4f}")
    print(f"Cos({angle_degrees}) = {cos_val:.4f}")
    print(f"Tan({angle_degrees}) = {tan_val:.4f}")

except ValueError:
    print("Invalid input! Please enter a valid number for the angle.")
