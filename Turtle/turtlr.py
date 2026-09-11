import turtle

# Create a turtle
t = turtle.Turtle()

# Set turtle shape and color
t.shape("turtle")
t.color("blue")

# Move forward and backward
t.forward(100)
t.backward(50)

# Turn right and left
t.right(90)
t.left(45)

# Change pen color
t.color("red")

# Put the pen down and draw
t.pendown()
t.forward(100)

# Pick up the pen
t.penup()
t.forward(50)

# Using up() and down()
t.up()
t.forward(50)
t.down()

# Draw a line
t.forward(100)

# Change fill color
t.fillcolor("yellow")

# Start filling a shape
t.begin_fill()

# Draw a square
for i in range(4):
    t.forward(100)
    t.right(90)

# Finish filling
t.end_fill()

# Move to a specific position
t.penup()
t.goto(0, 0)
t.pendown()

# Change direction
t.right(90)

# Draw a dot
t.dot()

# Leave a turtle stamp
t.stamp()

# Get current heading
print("Current heading:", t.heading())

# Get current position
print("Current position:", t.position())

# Keep the window open
turtle.done()