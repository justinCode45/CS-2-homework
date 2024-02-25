

import turtle
from turtle import Turtle
import math

def fasterChangeColor(t: Turtle, r: int, g: int, b: int) -> None:
    t._newLine()
    temp = t._colorstr((r, g, b)) 
    t._fillcolor = temp
    t._pencolor = temp
    t._update()

t = turtle.Turtle()
t.pensize(10)

turtle.colormode(255)

screen = turtle.Screen()
turtle.tracer(1, 100)

def num_to_rgb(val, max_val=3):
    i = (val * 255 / max_val)
    r = round(math.sin(0.024 * i + 0) * 127 + 128)
    g = round(math.sin(0.024 * i + 2) * 127 + 128)
    b = round(math.sin(0.024 * i + 4) * 127 + 128)
    return (r,g,b)

print (turtle.delay())


print (screen._tracing)
for i in range(10000):
    fasterChangeColor(t, *num_to_rgb(i))
    # t.color(num_to_rgb(i))
    t.forward(100)
    # t._newLine()    
    t.left(123)

print (screen._tracing)
turtle.done()