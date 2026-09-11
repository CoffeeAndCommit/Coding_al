import turtle

t = turtle.Turtle()
t.speed(0)

colors = ["red", "blue", "green", "purple", "orange"]

for i in range(60):
    t.color(colors[i % 5])
    t.forward(i * 3)
    t.right(144)

turtle.done()