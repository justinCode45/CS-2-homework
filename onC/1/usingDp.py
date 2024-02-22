from dp import *
import turtle

t = turtle.Turtle()
t.up()
t.backward(200)
t.left(90)
t.down()

drawPolygon(t, 100, 4)
t.color("red")
drawPolygon(t, 100, 8)
t.color("blue")
drawPolygon(t, 20, 20)