'''
.fillcolor()
.begin_fill()
.end_fill()

drawing logic should be betwwen begin and end
'''
import turtle

t= turtle.Turtle()
sides = 4
angle = 360.0/sides

t.fillcolor('red')
t.begin_fill()
for i in range(sides):
    t.forward(50)
    t.left(angle)

t.end_fill()
turtle.done()