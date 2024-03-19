# File Name : HW4_112652044.py
# Author : Justin Chen
# Email Address : justin.sc12@nycu.edu.tw
# HW Number : 4
# Description :
# Last Changed : 2024/3/17
# Dependencies : Python 3.12.2
# Additional :


import turtle
import math


def getInputs() -> list[int]:
    instring = input("Please enter the squence of intergr in [1,99] : ")
    inlist = instring.split()
    inlist = [int(x) for x in inlist]
    return inlist


def freqTable(alist: list[int]) -> dict[int, int]:
    freq = {}
    for i in alist:
        freq[i] = freq.get(i, 0) + 1

    sorted_freq = dict(sorted(freq.items()))

    return sorted_freq


def drawAxis(wn: turtle.Screen, freq: dict[int, int]):
    # Draw the axis
    
    chartxSize = len(freq) 
    chartySize = max(freq.values())
    t = turtle.RawTurtle(wn)
    t.speed(0)
    t.hideturtle()

    t.pensize(3)

    t.teleport(0, 0)
    t.setheading(90)
    t.forward(chartySize*1.05)
    t.write("Frequency")
    
    t.teleport(0, 0)
    t.setheading(0)
    t.forward(chartxSize*1.05)
    t.write("Value")
    

def drawBars(wn: turtle.Screen, freq: dict[int, int]):
    # Draw the bars
    t = turtle.RawTurtle(wn)
    t.speed(0)
    t.teleport(0.5, 0)
    t.hideturtle()
    t.color("blue")
    t.fillcolor("blue")

    for key, value in freq.items():
        t.begin_fill()
        t.left(90)
        t.forward(value)
        t.write(f"{value}", font=("Arial", 12, "normal"))
        t.right(90)
        t.forward(0.5)
        t.right(90)
        t.forward(value)
        t.left(90)
        t.end_fill()

        pos = t.pos()
        t.teleport(pos[0]-0.25, pos[1] - 0.5)
        t.write(f"{key}", font=("Arial", 12, "normal"))
        t.teleport(pos[0], pos[1])

        t.penup()
        t.forward(0.5)
        t.pendown()


def drawfreqTable(freq: dict[int, int]):

    # Set up the window
    wn = turtle.Screen()
    chartxSize = len(freq) 
    chartySize = max(freq.values())
    wn.setworldcoordinates(-chartxSize*0.05, -chartySize*0.05,
                           chartxSize*1.1, chartySize*1.1)
    # Draw the axis
    drawAxis(wn, freq)

    # Draw the bars
    drawBars(wn, freq)

    wn.update()

    wn.exitonclick()
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

    if len(alistFreq) > 10:
        alistFreq = sorted(alistFreq.items(), key=lambda x: x[1])
        alistFreq = dict(alistFreq[:5] +alistFreq[-5:])
    drawfreqTable(alistFreq)


    aga = input("Do you want to continue? (yes/no) : ")
    if aga == "yes":
        main()
    else:
        print("Goodbye!")

if __name__ == "__main__":
    main()
