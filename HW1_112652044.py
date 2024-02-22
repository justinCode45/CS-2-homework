# File Name : HW1_112652044.py
# Author : Justin Chen
# Email Address : justin.sc12@nycu.edu.tw
# HW Number : 1
# Description : This program will draw a square with turtle and the size of the square will be 50 and 60.
# Last Changed : 2019/10/07


import turtle



SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400


turtle.screensize(SCREEN_WIDTH, SCREEN_HEIGHT)
turtle.setworldcoordinates(0,SCREEN_HEIGHT,SCREEN_WIDTH,0)

# turList : turtle.Turtle = []
# for i in range(5):
#     turList.append(turtle.Turtle())
#     turList[i].speed(10)
#     turList[i].up()


# turList[0].goto(0,0)

# turList[0].down()
# turList[0].goto(800,400)
# turList[0].goto(0,0)
# turList[0].goto(800,400)
# turList[0].goto(0,0)

t = turtle.Turtle()
t.speed(10)
t.goto(0,0)
t.goto(800,400)
t.goto(0,400)

turtle.exitonclick()

