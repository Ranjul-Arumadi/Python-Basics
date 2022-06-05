import turtle
import random

t = turtle.Turtle()
t.speed(0)
sides = 6
angle = 360.0/sides
repeat = 5
colors = ['red', 'green','blue']

while repeat>0:
    for i in range(sides):
        t.color(random.choice(colors))
        t.width(5)
        t.forward(25)
        t.left(angle)
    repeat -= 1
    t.left(angle+10)

turtle.done()