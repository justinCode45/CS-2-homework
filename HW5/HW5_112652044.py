# File Name : HW5_112652044.py
# Author : Justin Chen
# Email Address : justin.sc12@nycu.edu.tw
# HW Number : 5
# Description :
# Last Changed : 2024/3/27
# Dependencies : Python 3.12.2
# Additional :

import csv
import turtle
from turtle import Vec2D


WIDTH = 1280
HEIGHT = 720


def moveTurtle(t: turtle.RawTurtle, x: float, y: float):
    t.penup()
    t.goto(x, y)
    t.pendown()


def getQuakeData() -> list[dict]:
    quakeData = []
    with open("tw2023Quake.csv", "r") as f:
        reader = csv.reader(f)
        header = next(reader)
        for row in reader:
            quakeData.append(dict(zip(header, row)))
    return quakeData


def drawAxis(t: turtle.RawTurtle, origin: Vec2D, width: int, height: int):
    t.speed(0)
    t.hideturtle()

    t.pensize(3)

    moveTurtle(t, origin[0], origin[1])
    t.setheading(90)
    t.forward(height)
    t.write("Quake Magnitude",font=("Arial", 12, "normal"))

    moveTurtle(t, origin[0], origin[1])
    t.setheading(0)
    t.forward(width)
    t.write("Quake Depth", font=("Arial", 12, "normal"))


def mapInRange(value: float, inMin: float, inMax: float, outMin: float, outMax: float) -> float:
    return (value - inMin) * (outMax - outMin) / (inMax - inMin) + outMin


def ScatterPlot(wn: turtle.Screen, origin: Vec2D, width: int, height: int, data: list[tuple[float, float]]):
    # Draw the axis
    t = turtle.RawTurtle(wn)
    wn.colormode(255)
    drawAxis(t, origin, width, height)
    maxX = max(data, key=lambda x: x[0])[0]
    maxY = max(data, key=lambda x: x[1])[1]
    minX = min(data, key=lambda x: x[0])[0]
    minY = min(data, key=lambda x: x[1])[1]
    # draw the axis scale min max and middle

    t.color(255, 0, 0)
    for d in data:
        x = mapInRange(d[0], minX, maxX, origin[0]+30, origin[0] + width - 30)
        y = mapInRange(d[1], minY, maxY, origin[1]+30, origin[1] + height - 30)
        moveTurtle(t, x, y)
        t.dot(7)


def app(quakeData: list[dict]):
    wn = turtle.Screen()
    wn.setup(WIDTH, HEIGHT)
    wn.setworldcoordinates(0, 0, WIDTH, HEIGHT)
    wn.title("Quake Graph")

    ScatterPlot(wn, Vec2D(50, 50), 600, 600,
                [(float(q["depth"]), float(q["mag"])) for q in quakeData])

    wn.mainloop()


def main():
    quakeData: list[dict] = getQuakeData()
    app(quakeData)


if __name__ == "__main__":
    main()
