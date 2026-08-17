from turtle import *

speed(0)
bgcolor("black")
setposition(-40, -30)
color("aqua")
tracer(3,0)

hideturtle()

for i in range(200):
    rt(i)
    circle(150,i)
    fd(70)
    right(270)
    fd(i)
    lt(1)

done()

