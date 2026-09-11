import turtle

t = turtle.Turtle()
t.speed(0)

colors = ["red", "blue", "purple", "pink", "orange"]

for i in range(36):
    t.color(colors[i % 5])
    t.circle(80)
    t.right(10)

turtle.done()