def drawSquare(t, sz):
    for i in range(4):
        t.forward(sz)
        t.left(90)

import turtle

alex = turtle.Turtle()

drawSquare(alex, 50)

