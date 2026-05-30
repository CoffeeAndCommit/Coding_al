# 1) Import the `turtle` library to draw using the turtle graphics window.
import turtle

# 2) Set the turtle screen background color to "Aqua".
turtle.bgcolor("Aqua")

# 3) Create a Turtle object and store it in `board`.
#    (This turtle will draw the star shape.)
board = turtle.Turtle()
# Change the drawing speed (1=slowest, 10=fast, 0=fastest)
board.speed(10)
board.fillcolor("yellow")
board.pencolor("red")

# Move the turtle to center the star on the screen
board.penup()
board.goto(-50, -25)
board.pendown()

# 4) Draw the first triangle:
board.begin_fill()
#    a) Move forward 100 units to draw the base.
board.forward(100)
#    b) Turn left 120 degrees and move forward 100 units.
board.left(120)
board.forward(100)
#    c) Turn left 120 degrees and move forward 100 units.
board.left(120)
board.forward(100)
board.end_fill()
#    (This completes an equilateral triangle.)

# 5) Lift the pen up using `penup()` so the turtle can move without drawing.
board.penup()

# 6) Reposition the turtle to start the second triangle:
#    a) Turn right 150 degrees.
board.right(150)
#    b) Move forward 50 units.
board.forward(50)

# 7) Put the pen down using `pendown()` to start drawing again.
board.pendown()

# 8) Draw the second triangle:
board.begin_fill()
#    a) Turn right 90 degrees and move forward 100 units.
board.right(90)
board.forward(100)
#    b) Turn right 120 degrees and move forward 100 units.
board.right(120)
board.forward(100)
#    c) Turn right 120 degrees and move forward 100 units.
board.right(120)
board.forward(100)
board.end_fill()
#    (This overlaps with the first triangle to form a star shape.)

# Redraw the first triangle so its red borders are fully visible over the yellow fill!
board.penup()
board.goto(-50, -25)
board.setheading(0)
board.pendown()
board.forward(100)
board.left(120)
board.forward(100)
board.left(120)
board.forward(100)

# 9) Call `turtle.done()` to keep the turtle window open after drawing finishes.
turtle.done()