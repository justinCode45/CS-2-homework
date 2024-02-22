import turtle

def drawPolygon(t: turtle.Turtle, length, n):
    angle = 360/n
    for i in range(n):
        t.forward(length)
        t.left(angle)
