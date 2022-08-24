import turtle

t = turtle.Turtle()

ps = 5
ts = 3
pa = 360/5
ta = 360/3

for i in range(ps):
    t.forward(10)
    t.right(pa)
    for j in range(ts):
        t.forward(10)
        t.left(ta)
