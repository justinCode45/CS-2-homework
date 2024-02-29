import turtle
import random
import math 

def showMontePi(n):
    wn = turtle.Screen()
    t = turtle.Turtle()
    wn.setworldcoordinates(-2,-2,2,2)

    t.up()
    t.goto(-1,0)
    t.down()
    t.goto(1,0)

    t.up()
    t.goto(0,1)
    t.down()
    t.goto(0,-1)

    inCircle = 0
    t.up()

    for i in range(n):
        x = random.random()
        y = random.random()
        t.goto(x,y)
        d = math.sqrt(x**2 + y**2)
        if d <= 1:
            inCircle += 1
            t.color("blue")
        else:
            t.color("red")
        t.dot()
    pi = inCircle/n*4
    wn.exitonclick()
    return pi

print(showMontePi(1000))