import turtle


t = turtle.Turtle()
t.speed(0)
t.goto(0,0)
colors = ["red", "green", "blue"]

for r in range (1, 4):
    t.color(colors[r-1])
    for i in range(0, 36):
        t.left(10)
        for j in range(0, 4):
            t.forward(25*r)
            t.left(90)