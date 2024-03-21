# File Name : HW4_112652044.py
# Author : Justin Chen
# Email Address : justin.sc12@nycu.edu.tw
# HW Number : 4
# Description :
# Last Changed : 2024/3/17
# Dependencies : Python 3.12.2
# Additional :


import turtle
from turtle import Vec2D
# import math


def moveTurtle(t: turtle.RawTurtle, x: float, y: float):
    t.penup()
    t.goto(x, y)
    t.pendown()

def getInputs() -> list[int]:
    instring = input(
        "Please enter the squence of intergr in [1,99] (at most 20 numbers) : ")
    inlist = instring.split()
    inlist = [int(x) for x in inlist]
    return inlist


def freqTable(alist: list[int]) -> dict[int, int]:
    freq = {}
    for i in alist:
        freq[i] = freq.get(i, 0) + 1

    sorted_freq = dict(sorted(freq.items()))

    return sorted_freq


def drawAxis(wn: turtle.Screen, origin: Vec2D, freq: dict[int, int]):
    # Draw the axis

    t = turtle.RawTurtle(wn)
    t.speed(0)
    t.hideturtle()

    t.pensize(3)

    moveTurtle(t, origin[0], origin[1])
    t.setheading(90)
    t.forward(600)
    t.write("Frequency")

    moveTurtle(t, origin[0], origin[1])
    t.setheading(0)
    t.forward(792)
    t.write("Value")


def drawBars(wn: turtle.Screen, origin: Vec2D, freq: dict[int, int]):
    # Draw the bars
    t = turtle.RawTurtle(wn)
    
    t.speed(0)
    moveTurtle(t, origin[0], origin[1])
    t.setheading(0)
    t.hideturtle()

    scaler = 550 / (max(freq.values()) )
    oneUnit = 720 / len(freq)
    t.forward(oneUnit/2)
    maxVal = max(freq.values())

    for key, value in freq.items():
        t.color((int)(255*value/maxVal), 128, 128)
        t.fillcolor((int)(255*value/maxVal), 128, 128)
        t.begin_fill()
        t.left(90)
        t.forward(value *scaler)
        t.write(f"{value}", font=("Arial", 10, "normal"))
        t.right(90)
        t.forward(oneUnit* 2/3)
        t.right(90)
        t.forward(value *scaler)
        t.left(90)
        t.end_fill()

        pos = t.pos()
        t.teleport(pos[0]-(oneUnit/2), pos[1] - 25)
        t.write(f"{key}", font=("Arial", 10, "normal"))
        t.teleport(pos[0], pos[1])

        t.penup()
        t.forward(oneUnit* 1/3)
        t.pendown()


def onclickf(x, y):
    
    pass

def app(freq: dict[int, int]):

    turtle.colormode(255)

    # Set up the window
    wn = turtle.Screen()
    wn.setup(1280,720)
    wn.setworldcoordinates(0,0,1280,720)

    origin = Vec2D(20, 20)
    # Draw the axis
    drawAxis(wn, origin, freq)
    # Draw the bars
    drawBars(wn, origin, freq)
    turtle.onclick(onclickf)

    turtle.mainloop()
    turtle.TurtleScreen._RUNNING = True


def main():

    print("This program can visualize the frequency of the input sequence.")
    p1 = getInputs()
    p2 = getInputs()
    p3 = getInputs()
    print("Echo the input sequence:")
    print(p1)
    print(p2)
    print(p3)
    print()
    alist = p1 + p2 + p3
    alist.sort()
    print(alist)
    alistFreq = freqTable(alist)
    print(alistFreq)

    # if len(alistFreq) > 10:
    #     alistFreq = sorted(alistFreq.items(), key=lambda x: x[1])
    #     alistFreq = dict(alistFreq[:5] + alistFreq[-5:])
    alistFreq =  dict(sorted(alistFreq.items(), key=lambda x: x[1]))
    app(alistFreq)

    aga = input("Do you want to continue? (yes/no) : ")
    if aga == "yes":
        main()
    else:
        print("Goodbye!")


if __name__ == "__main__":
    main()
