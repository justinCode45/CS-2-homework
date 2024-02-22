import turtle
def drawSquare(t: turtle.Turtle, sz):
    for i in range(4):
        t.forward(sz)
        t.left(90)

import time

turtle.speed(1)

alex = turtle.Turtle()



drawSquare(alex, 50)
drawSquare(alex, 60)

time.sleep(10)
