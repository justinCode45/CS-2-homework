from dp import *

def drawCircle (t:turtle.Turtle, radius:float):
    circumference = 2 * 3.14159 * radius
    sidelength = circumference / 360
    drawPolygon(t, sidelength, 360)

