# File Name : HW1_112652044.py
# Author : Justin Chen
# Email Address : justin.sc12@nycu.edu.tw
# HW Number : 1
# Description : This program will draw a square with turtle and the size of the square will be 50 and 60.
# Last Changed : 2024/2/24


import turtle
from turtle import Turtle
import math
from math import cos, sin
import cv2
import numpy as np
import random
import time


SCREEN_WIDTH = 1580
SCREEN_HEIGHT = 720
screen = turtle.Screen()


def setupScreen() -> None:
    screen.screensize(SCREEN_WIDTH, SCREEN_HEIGHT)
    screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    screen.setworldcoordinates(0,0,SCREEN_WIDTH,SCREEN_HEIGHT)

def drawSquare(t: Turtle, o: tuple[float], r: tuple[float]) -> None:
    moveTurtle(t, o)
    t.goto(r[0],o[1])
    t.goto(r)
    t.goto(o[0],r[1])
    t.goto(o)
    t.up()    

def drawDivider(t: Turtle) -> None:
    drawSquare(t, (0,0), (SCREEN_WIDTH, SCREEN_HEIGHT))
    moveTurtle(t, (0, SCREEN_HEIGHT//3))
    t.goto(300, SCREEN_HEIGHT//3)
    moveTurtle(t, (0, 2*SCREEN_HEIGHT//3))
    t.goto(300, 2*SCREEN_HEIGHT//3)
    moveTurtle(t, (300, 0))
    t.goto(300, SCREEN_HEIGHT)

def moveTurtle(t: Turtle, dest: tuple[float]) -> None:
    t.up()
    t.goto(dest)
    t.down()

def peanoCurve(t: Turtle, dirction: bool, order: int, length: float) -> None:
    '''
    Draw a Peano curve using turtle graphics.

    Parameters:
    t (Turtle): The turtle object used for drawing.
    dirction (bool): The direction of the curve. 1 for right, 0 for left.
    order (int): The order of the curve. Determines the complexity of the curve.
    length (float): The length of each segment of the curve.

    Returns:
    None
    '''
    mapD = lambda x: 1 if x else -1

    if order == 1: 
        t.forward(length)
        t.right(90 * mapD(dirction))
        t.forward(length)
        t.right(90 * mapD(dirction))
        t.forward(length)
        return
    
    d = 2.6
    forwardLen = length / (d ** (order - 1))

    peanoCurve(t, not dirction, order - 1, length / d)
    if order % 2 == 0:
        t.right(90 * mapD(dirction))
        t.forward(forwardLen)
    else:
        t.forward(forwardLen)
        t.right(90 * mapD(dirction))
    peanoCurve(t, dirction, order - 1, length / d)
    if order % 2 == 0:
        t.left(90 * mapD(dirction))
        t.forward(forwardLen)
        t.left(90 * mapD(dirction))
    else: 
        t.forward(forwardLen)
    peanoCurve(t, dirction, order - 1, length / d)
    if order % 2 == 0:
        t.forward(forwardLen)
        t.right(90 * mapD(dirction))
    else:
        t.right(90 * mapD(dirction))
        t.forward(forwardLen)
    peanoCurve(t, not dirction, order - 1, length / d)

def cardioid(t: Turtle, r: float, n: int, v: int = 2) -> None:
    '''
    Draw a cardioid using turtle graphics.

    Parameters:
    t (Turtle): The turtle object used for drawing.
    r (float): The radius of the cardioid.
    n (int): The number of points used to draw the cardioid.

    Returns:
    None
    '''
    w = 2 * math.pi / n
    origin = t.pos()-(r, 0)
    suporigin = lambda t: origin + (2*r*cos(w*t), 2*r*sin(w*t))
    turtlepos = lambda t: suporigin(t) + (r*cos(v*w*t+math.pi), r*sin(v*w*t+math.pi))
    for i in range(n):
        t.goto(turtlepos(i+1))

def drawequilateralTriangle(t: Turtle, r: float) -> None:
    o = t.pos()
    t.goto(o[0]+r, o[1])
    t.goto(o[0]+r/2, o[1]+r*math.sqrt(3)/2)
    t.goto(o)

def randomPointonRect(o: tuple[float], r: tuple[float]) -> tuple[float]:
    # generate a random point on the rectangle side 
    # o: origin, r: right top
    # return: (x, y)
    w = r[0] - o[0]
    h = r[1] - o[1]
    if random.random() < w / (w + h):
        # w
        return (random.uniform(o[0], r[0]), random.choice([o[1], r[1]]))
    else:
        return (random.choice([o[0], r[0]]), random.uniform(o[1], r[1]))

def length(p1: tuple[float], p2: tuple[float]) -> float:
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)
    
def drawImage(t: Turtle, path: str) -> None:
    img = cv2.imread(path)
    sH = (720*10) / img.shape[0]
    sW = (1280*10) / img.shape[1]  
    scaler = sW if sW < sH else sH 
    img = cv2.resize(img,None,fx=scaler, fy=scaler, interpolation = cv2.INTER_CUBIC)
    torigin = (0,0)
    tmax =(0,0)

    print (img.shape)
    print (300 + (1280-img.shape[1]/10)/2)
    if sH < sW : # W  ss
        torigin = (300 + (1280-img.shape[1]/10)/2, 0)
        tmax = (torigin[0] + img.shape[1]/10 , 720)
    else: # H ss
        torigin = (300,(720-img.shape[0]/10)/2)
        tmax = (1580, torigin[1] + img.shape[0]/10)
    
    print (torigin, tmax)
    moveTurtle(t, torigin)

    t.pensize(3)
    turtle.tracer(2000, 0)

    for _ in range(3000):
        p1 = randomPointonRect(torigin, tmax)
        p2 = randomPointonRect(torigin, tmax)
        if (p1[0] - p2[0]) * (p1[1] - p2[1]) == 0:
            continue
        moveTurtle(t, p1)
        t.setheading( t.towards(p2) )
        delta = 5 
        while 1 :
            samplePoint = ((t.pos()[0]+0.5*delta*cos(t.heading())), t.pos()[1]+0.5*delta*sin(t.heading()))
            if samplePoint[0] > tmax[0] or samplePoint[0] < torigin[0] or samplePoint[1] > tmax[1] or samplePoint[1] < torigin[1]:
                break
            samplePoint = ((samplePoint[0]-torigin[0])*10, (samplePoint[1]-torigin[1])*10)
            sampleX = int(samplePoint[0])
            sampleY = int(samplePoint[1])
            sampleY = img.shape[0] - sampleY
            if sampleX > img.shape[1]-1 or sampleY > img.shape[0]-1 or sampleX <= 0 or sampleY <= 0:
                break
            color = img[sampleY][sampleX]
            t.color(color[2], color[1], color[0])
            t.forward(delta)
            
    t.pensize(1)
    turtle.update()


def main():
    
    random.seed(time.time())
    setupScreen()

    t = Turtle()
    turtle.tracer(30, 1)
    turtle.colormode(255)
    drawDivider(t)

    moveTurtle(t, (55, 500))
    t.left(90)
    peanoCurve(t, 1, 5, 300)

    moveTurtle(t, (230, 360))
    cardioid(t, 40, 500,2)

    moveTurtle(t, (55, 40))
    drawequilateralTriangle(t, 200)
    turtle.update()

    drawImage(t, "lico.jpg")

    turtle.update()
    screen.exitonclick()

if __name__ == "__main__":
    main()