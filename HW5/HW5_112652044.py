# File Name : HW5_112652044.py
# Author : Justin Chen
# Email Address : justin.sc12@nycu.edu.tw
# HW Number : 5
# Description :
# Last Changed : 2024/3/27
# Dependencies : Python 3.12.2
# Additional :
#   1. Click on the dot to see the detail of the data
# Note:
#   1. Please install chinese font in your system, or the chinese character will not be displayed correctly
#   2. Set the data file name to DATAFILE.
#   3. Set the key of magnitude to KEYOFMAG.
#   4. Set the key of depth to KEYOFDEPTH.
import csv
import turtle
from turtle import Vec2D
from urllib import request

KEYOFMAG = "mag"
# KEYOFMAG = "magnitude"
KEYOFDEPTH = "depth"
DATAFILE = "tw2023Quake.csv"
# DATAFILE = "t.csv"

WIDTH = 1280
HEIGHT = 720


def get_quake_data(year: int) -> list[dict]:
    url = "https://earthquake.usgs.gov/fdsnws/event/1/query"
    params = {
        "format": "csv",
        "starttime": f"{year}-01-01",
        "endtime": f"{year}-01-02",
        "minlatitude": 21.9267,
        "maxlatitude": 24.9571,
        "minlongitude": 119.8579,
        "maxlongitude": 123.0428,
        "minmagnitude": 4.5,
    }
    response = request.urlopen(
        url + "?" + "&".join([f"{k}={v}" for k, v in params.items()]))
    reader = csv.reader(response.read().decode().splitlines())
    header = next(reader)
    quake_data = [dict(zip(header, row)) for row in reader]
    return quake_data


class Box:
    def __init__(self, x: int, y: int, width: int, height: int, wn: turtle.Screen):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.wn = wn

    def clicked(self, x: int, y: int) -> bool:
        if self.x < x < self.x + self.width and self.y < y < self.y + self.height:
            return True
        return False

    def do():
        pass


class Label(Box):
    def __init__(self, x: int, y: int, width: int, height: int, wn: turtle.Screen, texti: str = ""):
        super().__init__(x, y, width, height, wn)
        self.text = texti
        self.t = turtle.RawTurtle(wn)
        self.t.hideturtle()

    def draw(self):
        self.t.clear()
        self.t.hideturtle()
        self.t.speed(0)
        self.t.penup()
        self.t.goto(self.x, self.y)
        self.t.write(self.text, font=("Courier", 11, "normal"))
        self.wn.update()


def PPMCC(x: list[float], y: list[float]) -> float:
    n = len(x)
    sum_x = sum(x)
    sum_y = sum(y)
    sum_x2 = sum([i**2 for i in x])
    sum_y2 = sum([i**2 for i in y])
    sum_xy = sum([i*j for i, j in zip(x, y)])
    return (n*sum_xy - sum_x*sum_y) / ((n*sum_x2 - sum_x**2)*(n*sum_y2 - sum_y**2))**0.5


def moveTurtle(t: turtle.RawTurtle, x: float, y: float):
    t.penup()
    t.goto(x, y)
    t.pendown()


def getQuakeData() -> list[dict]:
    quakeData = []
    with open(DATAFILE, "r", encoding="utf8") as f:
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
    t.write("Quake Magnitude", font=("Arial", 12, "normal"))

    moveTurtle(t, origin[0], origin[1])
    t.setheading(0)
    t.forward(width)
    t.write("Quake Depth", font=("Arial", 12, "normal"))


def mapInRange(value: float, inMin: float, inMax: float, outMin: float, outMax: float) -> float:
    return (value - inMin) * (outMax - outMin) / (inMax - inMin) + outMin


def ScatterPlot(wn: turtle.Screen, origin: Vec2D, width: int, height: int, data: list[tuple[float, float]]) -> list[Box]:
    # Draw the axis

    boxlist = []
    t = turtle.RawTurtle(wn)
    wn.colormode(255)
    wn.tracer(0)
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
        boxlist.append(Box(x-5, y-5, 10, 10, wn))
        moveTurtle(t, x, y)
        t.dot(7)

    xaxis = []
    yaxis = []

    for i in range(10):
        yaxis.append(minY + (maxY - minY) / 9 * i)
    for i in range(5):
        xaxis.append(int(minX + (maxX - minX) / 4 * i))

    t.color(0, 0, 0)
    for i in xaxis:
        x = mapInRange(i, minX, maxX, origin[0] +
                       30, origin[0] + width - 30)
        moveTurtle(t, x, origin[1] - 5)
        t.setheading(90)
        t.forward(10)
        moveTurtle(t, x, origin[1] - 29)
        t.write(f"{i:g}", align="center", font=("Arial", 12, "normal"))

    for i in yaxis:
        y = mapInRange(i, minY, maxY, origin[1]+30, origin[1] + height - 30)
        moveTurtle(t, origin[0] - 10, y)
        t.setheading(0)
        t.forward(20)
        moveTurtle(t, origin[0] - 30, y-10)
        t.write(f"{i:.1f}", align="center", font=("Arial", 12, "normal"))

    wn.update()
    return boxlist


def freqTable(alist: list[float]) -> dict[int, int]:
    freq = {}
    for i in alist:
        freq[i] = freq.get(i, 0) + 1

    sorted_freq = dict(sorted(freq.items()))
    return sorted_freq


def strengthOfPPMCC(ppmcc: float) -> str:
    if ppmcc == 1:
        return "Perfect Positive Correlation"
    elif ppmcc == -1:
        return "Perfect Negative Correlation"
    elif ppmcc >= 0.5:
        return "Strong Positive Correlation"
    elif ppmcc <= -0.5:
        return "Strong Negative Correlation"
    elif ppmcc > 0:
        return "Weak Positive Correlation"
    elif ppmcc < 0:
        return "Weak Negative Correlation"
    else:
        return "No Correlation"


class APP():

    def __init__(self, _quakeData: list[dict]):
        self.quakeData = _quakeData
        self.wn = turtle.Screen()
        self.pointlist: list[Box] = []
        self.buttonlist = []
        self.lable = Label(800, 100, 300, 100, self.wn,
                           "Click on the dot to see the data")
        self.wn.setup(WIDTH, HEIGHT)
        self.wn.setworldcoordinates(0, 0, WIDTH, HEIGHT)
        self.wn.title("Quake Graph")

    def draw(self):
        self.wn.clear()
        t = turtle.RawTurtle(self.wn)
        t.color(0, 0, 0)
        boxlist = ScatterPlot(self.wn, Vec2D(50, 50), 600, 600,
                              [(float(q[KEYOFDEPTH]), float(q[KEYOFMAG])) for q in self.quakeData])
        ppmcc = PPMCC([float(q[KEYOFDEPTH]) for q in self.quakeData],
                      [float(q[KEYOFMAG]) for q in self.quakeData])
        strengthPPMCC = strengthOfPPMCC(ppmcc)
        moveTurtle(t, 900, 600)
        t.write(f"PPMCC: {ppmcc:.4f}", align="center",
                font=("Arial", 12, "normal"))
        moveTurtle(t, 900, 570)
        t.write(f"Strength: {strengthPPMCC}",
                align="center", font=("Arial", 12, "normal"))
        self.pointlist = boxlist
        self.lable.draw()
        self.wn.onclick(self.gen_handle_click())

    def run(self):
        self.draw()
        self.wn.mainloop()

    def gen_handle_click(self):
        maxkeylen = max([len(key) for key in self.quakeData[0].keys()])
        def handle_click(x: int, y: int):
            for point in self.pointlist:
                if point.clicked(x, y):
                    self.lable.text = ""
                    for key, value in self.quakeData[self.pointlist.index(point)].items():
                        self.lable.text += f"{key:{maxkeylen}}: {value}\n"
                    break

            self.lable.draw()
            self.wn.update()
            self.wn.onclick(handle_click)

        return handle_click


def main():
    print("This program will draw a scatter plot of the quake data")
    quakeData: list[dict] = getQuakeData()
    print(f"Total {len(quakeData)} earthquakes data loaded.")
    print("List of depth: ", end="")
    print([float(q[KEYOFDEPTH]) for q in quakeData])
    print("List of magnitude: ", end="")
    print([float(q[KEYOFMAG]) for q in quakeData])
    frqt = freqTable([float(q[KEYOFMAG]) for q in quakeData])
    print("Frequency Table of Magnitude: ")
    print(f"{"VALUE":>10}  |{"FREQUENCY":>10}")
    print(f"{"-"*12}|{"-"*10}")
    for key, value in frqt.items():
        print(f"{key:>10}  |{value:>10}")
    ppmcc = PPMCC([float(q[KEYOFDEPTH]) for q in quakeData],
                  [float(q[KEYOFMAG]) for q in quakeData])
    print("PPMCC: ", ppmcc)
    print("Strength: ", strengthOfPPMCC(ppmcc))

    app = APP(quakeData)
    app.run()


if __name__ == "__main__":
    main()
