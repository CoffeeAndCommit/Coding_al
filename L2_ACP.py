# Assignment: Area and Perimeter of Circle
# Create a Circle class constructed by a radius with methods
# to compute the area and perimeter of the circle.

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


# Taking radius as input from the user
r = float(input("Enter the radius of the circle: "))

# Creating a Circle object
c = Circle(r)

# Displaying results
print(f"\nRadius    : {c.radius}")
print(f"Area      : {c.area():.2f}")
print(f"Perimeter : {c.perimeter():.2f}")
