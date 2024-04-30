import math
import turtle


def drawTriangle(t, p1, p2, p3):
    p1 = (p1[0], p1[1])
    p2 = (p2[0], p2[1])
    p3 = (p3[0], p3[1])
    t.up()
    t.goto(p1)
    t.down()
    t.goto(p2)
    t.goto(p3)
    t.goto(p1)


def midPoint(p1, p2):
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)


def sierepinski(t, p1, p2, p3, depth):
    if depth == 0:
        drawTriangle(t, p1,p2,p3)
    else:
        m1 = midPoint(p1, p2)
        m2 = midPoint(p2, p3)
        m3 = midPoint(p1, p3)
        sierepinski(t, p1, m1, m3, depth-1)
        sierepinski(t, m1, p2, m2, depth-1)
        sierepinski(t, m3, m2, p3, depth-1)


t = turtle.Turtle()
t.speed(0)
t.up()
t.goto(-200, -200)
t.down()
p1 = (-200, -200)
p2 = (200, -200)
p3 = (0, math.sqrt(3) * 200 - 200)
sierepinski(t, p1, p2, p3, 6)
t.hideturtle()
turtle.mainloop()
