# File Name : HW4_112652044.py
# Author : Justin Chen
# Email Address : justin.sc12@nycu.edu.tw
# HW Number : 4
# Description :
# Last Changed : 2024/3/27
# Dependencies : Python 3.12.2
# Additional :
#   1. Colorful bars
#   2. Sort by value or frequency
#   3. Draw all or draw the smallest 5 and largest 5
#   4. Add number
# Thanks to 112652022 for the inspiration

import turtle
from turtle import Vec2D
import random


def moveTurtle(t: turtle.RawTurtle, x: float, y: float):
    t.penup()
    t.goto(x, y)
    t.pendown()

class Button:

    def __init__(self, wn: turtle.Screen, pos: Vec2D, width: int, height: int, text: str):
        self.pos = pos
        self.width = width
        self.height = height
        self.text = text
        self.wn = wn

    def clicked(self, x: int, y: int) -> bool:
        if self.pos[0] - self.width/2 < x < self.pos[0] + self.width/2 and self.pos[1] - self.height/2 < y < self.pos[1] + self.height/2:
            return True
        return False

    def draw(self):
        t = turtle.RawTurtle(self.wn)
        t.hideturtle()
        t.speed(0)
        t.penup()
        t.goto(self.pos)
        t.forward(self.width/2)
        t.pendown()
        t.right(90)
        t.forward(self.height/2)
        t.right(90)
        t.forward(self.width)
        t.right(90)
        t.forward(self.height)
        t.right(90)
        t.forward(self.width)
        t.right(90)
        t.forward(self.height)
        t.right(90)
        t.forward(self.width/2)
        t.write(self.text, align="center", font=("Arial", 10, "normal"))


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
    wn.colormode(255)
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
    lengthFeq = len(freq)
    wn.colormode(255)
    wn.tracer(lengthFeq//3, 0)
    t.speed(0)
    moveTurtle(t, origin[0], origin[1])
    t.setheading(0)
    t.hideturtle()

    scaler = 550 / (max(freq.values()))
    oneUnit = 720 / lengthFeq
    t.forward(oneUnit/2)
    maxVal = max(freq.values())

    for key, value in freq.items():
        t.color((int)(255*value/maxVal), 128, 128)
        t.fillcolor((int)(255*value/maxVal), 128, 128)
        t.begin_fill()
        t.left(90)
        t.forward(value * scaler)
        t.write(f"{value}", font=("Arial", 10, "normal"))
        t.right(90)
        t.forward(oneUnit * (0.5+0.5*lengthFeq/(lengthFeq+3)))
        t.right(90)
        t.forward(value * scaler)
        t.left(90)
        t.end_fill()

        pos = t.pos()
        moveTurtle(t,pos[0]-(oneUnit/2), pos[1] - 25)
        t.write(f"{key}", font=("Arial", 10, "normal"))
        moveTurtle(t,pos[0], pos[1])

        t.penup()
        t.forward(oneUnit * (0.5-0.5*lengthFeq/(lengthFeq+3)))
        t.pendown()
    
    wn.update()
    wn.tracer(1, 1)


def app(freq: dict[int, int]):

    print(f"{"VALUE":>10}  |{"FREQUENCY":>10}")
    print(f"{"-"*12}|{"-"*10}")
    for key,value in freq.items():
        print(f"{key:>10}  |{value:>10}")

    # Set up the window
    wn = turtle.Screen()
    wn.setup(1280, 720)
    wn.setworldcoordinates(0, 0, 1280, 720)
    wn.colormode(255)

    alistFreq = dict(sorted(freq.items()))
    if len(freq) > 10:
        alistFreq = sorted(freq.items(), key=lambda x: x[1])
        alistFreq = dict(alistFreq[:5] + alistFreq[-5:])

    origin = Vec2D(20, 20)
    drawAxis(wn, origin, alistFreq)
    drawBars(wn, origin, alistFreq)

    buttons = [Button(wn, Vec2D(1000, 600), 100, 50, "sort by frequency"),
               Button(wn, Vec2D(1000, 500), 100, 50, "Default mode"),
               Button(wn, Vec2D(1000, 400), 100, 50, "sort by value"),
               Button(wn, Vec2D(1000, 200), 100, 50, "Add number")]

    for button in buttons:
        button.draw()

    def onclickf(x, y):
        nonlocal freq
        flag = 0
        for i in range(len(buttons)):
            if buttons[i].clicked(x, y):
                flag = i+1
                break
        match flag:
            case 0:
                return
            case 1:
                wn.clear()
                drawAxis(wn, origin, freq)
                drawBars(wn, origin, freq)
            case 2:
                wn.clear()
                drawAxis(wn, origin, alistFreq)
                drawBars(wn, origin, alistFreq)
            case 3:
                wn.clear()
                freqValue = dict(sorted(freq.items(), key=lambda x: x[0]))
                drawAxis(wn, origin, freqValue)
                drawBars(wn, origin, freqValue)
            case 4:
                innum = wn.textinput("Add number", "Please enter a sequence of intergr in [1,99]")
                if innum is not None:
                    innum = [int(x) for x in innum.split() if x.isdigit()]
                    for i in range(len(innum)):
                        freq[innum[i]] = freq.get(innum[i], 0) + 1
                    freq = dict(sorted(freq.items(),key=lambda x: x[1]))
                    wn.clear()
                    drawAxis(wn, origin, freq)
                    drawBars(wn, origin, freq)

        for b in buttons:
            b.draw()
        wn.onclick(onclickf)

    wn.onclick(onclickf)
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
    

    alistFreq = dict(sorted(alistFreq.items(), key=lambda x: x[1]))
    app(alistFreq)

    aga = input("Do you want to continue? (yes/no) : ")
    if aga == "yes":
        main()
    else:
        print("Goodbye!")


if __name__ == "__main__":
    main()
