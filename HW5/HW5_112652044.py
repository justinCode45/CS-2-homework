# File Name : HW5_112652044.py
# Author : Justin Chen
# Email Address : justin.sc12@nycu.edu.tw
# HW Number : 5
# Description : This program will draw a scatter plot of the quake data
# Last Changed : 2024/4/7
# Dependencies : Python 3.12.2, turtle, numpy, network connection
# Additional :
#   1. Click on the dot to see the detail of the data
#   2. CLick on the "Get New Data" button to get new earthquake data
#   3. Neural Network to predict the magnitude of the earthquake
#      (Not work well...)
import csv
import turtle
from turtle import Vec2D
from urllib import request
import numpy as np

KEYOFMAG = "mag"
# KEYOFMAG = "magnitude"
KEYOFDEPTH = "depth"
DATAFILE = "tw2023Quake.csv"
# DATAFILE = "t.csv"

WIDTH = 1280
HEIGHT = 720


def get_quake_data(year: int, range=2) -> list[dict]:
    url = "https://earthquake.usgs.gov/fdsnws/event/1/query"
    params = {
        "format": "csv",
        "starttime": f"{year-range}-01-01",
        "endtime": f"{year}-12-02",
        "minlatitude": 21.9267,
        "maxlatitude": 24.9571,
        "minlongitude": 119.8579,
        "maxlongitude": 123.0428,
        "minmagnitude": 2.5,
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


class Button(Box):
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
        self.t.pendown()
        self.t.setheading(0)
        self.t.forward(self.width)
        self.t.setheading(90)
        self.t.forward(self.height)
        self.t.setheading(180)
        self.t.forward(self.width)
        self.t.setheading(270)
        self.t.forward(self.height)
        self.t.penup()
        self.t.goto(self.x + self.width//2, self.y + self.height//2)
        self.t.write(self.text, align="center",
                     font=("Arial", 12, "normal"))
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
        self.button_getNewData = Button(
            800, 50, 300, 50, self.wn, "Get New Data")
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
        self.button_getNewData.draw()
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
            if self.button_getNewData.clicked(x, y):
                self.quakeData = get_quake_data(2024)
                self.draw()

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
    print(f"{'VALUE':>10}  |{'FREQUENCY':>10}")
    print(f"{'-'*12}|{'-'*10}")
    for key, value in frqt.items():
        print(f"{key:>10}  |{value:>10}")
    ppmcc = PPMCC([float(q[KEYOFDEPTH]) for q in quakeData],
                  [float(q[KEYOFMAG]) for q in quakeData])
    print("PPMCC: ", ppmcc)
    print("Strength: ", strengthOfPPMCC(ppmcc))

    app = APP(quakeData)
    app.run()


def sigmoid(x):
    return 1/(1+np.exp(-x))


def sigmoid_derivative(x):
    return sigmoid(x)*(1-sigmoid(x))


def prepare_data():
    data = get_quake_data(2024, 30)
    dataR = []
    for q in data:
        dataR.append([np.array([[float(q['depth']), float(q['longitude']), float(q['latitude'])]]).T,
                      np.array([[float(q['mag'])/10]]).T])
    return dataR


def train_network(layer_size):
    data = prepare_data()
    # Randomly initialize weights and biases
    weights = [np.random.rand(layer_size[i+1], layer_size[i])
               for i in range(len(layer_size)-1)]
    biases = [np.array([np.random.rand(layer_size[i+1])]).T
              for i in range(len(layer_size)-1)]
    # Train the network
    for k in range(100):
        for d in data:
            zs = []
            a = d[0]
            activations: list[np.ndarray] = [a]
            # Forward pass
            for i in range(len(layer_size)-1):
                z = weights[i]@a + biases[i]
                zs.append(z)
                a = sigmoid(z)
                activations.append(a)
            # Backpropagation
            gradint_a: list[np.ndarray] = [[]
                                           for _ in range(len(layer_size)-1)]
            gradint_b: list[np.ndarray] = [[]
                                           for _ in range(len(layer_size)-1)]
            gradint_w: list[np.ndarray] = [[]
                                           for _ in range(len(layer_size)-1)]
            for i in range(len(layer_size)-2, -1, -1):
                if i == len(layer_size)-2:
                    gradint_a[i] = 2*(activations[-1] - d[1])
                else:
                    gradint_a[i] = (weights[i+1].T@gradint_b[i+1])
                gradint_b[i] = gradint_a[i]*sigmoid_derivative(zs[i])
                gradint_w[i] = np.dot(gradint_b[i], activations[i].T)
            # Update weights and biases
            for i in range(len(layer_size)-1):
                weights[i] -= gradint_w[i]
                biases[i] -= gradint_b[i]
        print(k)
    return weights, biases


def load_network():
    weightsTmp = np.load("weights.npz", allow_pickle=True)
    biasesTmp = np.load("biases.npz", allow_pickle=True)
    weights = []
    biases = []
    for i in weightsTmp:
        weights.append(weightsTmp[i])
    for i in biasesTmp:
        biases.append(biasesTmp[i])
    return weights, biases


def neural_network():
    layer_size = [3, 4, 1]
    try:
        weights, biases = load_network()
    except:
        weights, biases = train_network(layer_size)
        np.savez("biases.npz", *biases)
        np.savez("weights.npz", *weights)

    for _ in range(10):
        rawinput = input("Please enter depth, longitude, latitude(eg. 100 121 23):\n")
        rawinput = rawinput.strip()
        rawinput = rawinput.split(" ")
        rawinput = [float(i) for i in rawinput]
        a = np.array([rawinput]).T
        for i in range(len(layer_size)-1):
            a = sigmoid(weights[i]@a + biases[i])

        print(f"Magnitude prediction: {a[0][0]*10:.3f}")


if __name__ == "__main__":
    main()
    # Additional Function
    neural_network()
