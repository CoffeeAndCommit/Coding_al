# Assignment: Square
# Write a program to draw a square using the turtle library

import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("lightblue")
screen.title("Drawing a Square")

# Create a turtle object
pen = turtle.Turtle()
pen.color("purple")
pen.pensize(4)
pen.speed(3)

# Draw a square using a for loop
for _ in range(4):
    pen.forward(100)  # Move forward by 100 units (draws the side)
    pen.left(90)      # Turn left by 90 degrees (creates the corner)

# Keep the window open until the user clicks to close it
turtle.done()
