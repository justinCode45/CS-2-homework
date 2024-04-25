from math import acos, sin, cos, radians
from csv import reader
from random import sample
import turtle
from urllib import request
isNumpy = True
try:
    import matplotlib.pyplot as plt
    import matplotlib.animation as animation
    import numpy as np
except:
    isNumpy = False
    print("Numpy is not installed")


class Vec:
    def __init__(self, _coor: list[float]):
        self.__coor: list[float] = _coor
        self.__dim: int = len(_coor)

    def __getitem__(self, key: int) -> float:
        if key >= self.__dim:
            raise IndexError
        return self.__coor[key]

    def __truediv__(self, other: float):
        if other == 0:
            raise ZeroDivisionError
        return Vec([x/other for x in self.__coor])

    def __sub__(self, other: 'Vec'):
        if self.__dim != other.__dim:
            raise ValueError('Dimension mismatch')
        return Vec([self.__coor[i] - other.__coor[i] for i in range(self.__dim)])

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, Vec):
            return False
        return self.__coor == value.__coor

    def __add__(self, other: 'Vec'):
        if self.__dim != other.__dim:
            raise ValueError('Dimension mismatch')
        return Vec([self.__coor[i] + other.__coor[i] for i in range(self.__dim)])

    def __str__(self) -> str:
        return str(self.__coor)

    def dim(self) -> int:
        return self.__dim

    def norm(self) -> float:
        return sum([x**2 for x in self.__coor])**0.5


def GCD(first: Vec, second: Vec) -> float:
    delta_lon = abs(first[1] - second[1])
    fg = sin(radians(first[0])) * sin(radians(second[0])) + cos(
        radians(first[0])) * cos(radians(second[0])) * cos(radians(delta_lon))
    fg = max(-1, fg)
    fg = min(1, fg)
    dd = acos(fg)
    return dd


class Data():
    def __init__(self, _data: list[float], otherinfo: dict[str] = None):
        self.info: dict[str] = otherinfo
        self.cluster: int = -1
        self.coor = Vec(_data)


def readData(filename: str) -> list[Data]:
    with open(filename, 'r') as file:
        satareader = reader(file)
        header = next(satareader)
        latindex = header.index('latitude')
        lonindex = header.index('longitude')
        data = [Data([float(row[latindex]), float(row[lonindex])], zip(header, row))
                for row in satareader]
    return data


def get_quake_data(year: int, range=2) -> list[Data]:
    url = "https://earthquake.usgs.gov/fdsnws/event/1/query"
    params = {
        "format": "csv",
        "starttime": f"{year-range}-01-01",
        "endtime": f"{year}-12-02",
        "minmagnitude": 5,
    }
    print(url + "?" + "&".join([f"{k}={v}" for k, v in params.items()]))
    response = request.urlopen(
        url + "?" + "&".join([f"{k}={v}" for k, v in params.items()]))
    datareader = reader(response.read().decode().splitlines())

    header = next(datareader)
    latindex = header.index('latitude')
    lonindex = header.index('longitude')
    data = [Data([float(row[latindex]), float(row[lonindex])], zip(header, row))
            for row in datareader]
    return data


def kmeans(datalist: list[Data], k: int, repeat: int) -> tuple[list[Data], list[Vec], bool]:
    dim = datalist[0].coor.dim()
    centroidsD: list[Data] = sample(datalist, k)
    centroids: list[Vec] = [c.coor for c in centroidsD]
    stable: bool = False
    for ii in range(repeat):
        new_centroids: list[Vec] = [Vec([0 for _ in range(dim)])
                                    for _ in range(k)]
        centroids_count: list[int] = [0 for _ in range(k)]
        for data in datalist:
            data.cluster = min(range(k),
                               key=lambda i: GCD(data.coor, centroids[i]))
            new_centroids[data.cluster] += data.coor
            centroids_count[data.cluster] += 1
        new_centroids = [new_centroids[i] / centroids_count[i] if centroids_count[i] != 0 else centroids[i]
                         for i in range(k)]
        if centroids == new_centroids:
            stable = True
            break
        centroids = new_centroids
    return datalist, centroids, stable


def color(i: int) -> str:
    colors = ['red', 'blue', 'green', 'yellow', 'purple',
                'orange', 'brown', 'pink', 'gray', 'black']
    return colors[i]
def draw_map(data: list[Data], centroids: list[Vec]):
    t = turtle.Turtle()
    wn = turtle.Screen()
    wn.setup(1080, 544)
    t.speed(0)
    wn.tracer(0)
    t.hideturtle()
    wn.setworldcoordinates(-180, -90, 180, 90)
    wn.bgpic("world.png")
    for d in data:
        t.penup()
        t.goto(d.coor[1], d.coor[0])
        t.pendown()
        t.dot(5, color(d.cluster))
    wn.update()
    wn.exitonclick()
    turtle.TurtleScreen._RUNNING = True


def transCoord(lat: float, lon: float) -> Vec:
    x = cos(radians(lat)) * cos(radians(lon))
    y = cos(radians(lat)) * sin(radians(lon))
    z = sin(radians(lat))
    return Vec([x, y, z, 0])

    
def draw_3Dmap(data: list[Data], centroids: list[Vec]):
    for d in data:
        d.coor = transCoord(d.coor[0], d.coor[1])
    for c in centroids:
        c = transCoord(c[0], c[1])
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    for d in data:
        ax.scatter(d.coor[0], d.coor[1], d.coor[2], c=color(d.cluster))
    #rotation animation
    def update(num, data, ax):
        ax.view_init(elev=10, azim=num)
    ani = animation.FuncAnimation(fig, update, frames=range(0, 360, 2), fargs=(data, ax))
    # plt.show()
    print('Saving gif...')
    ani.save('quakes.gif', writer='pillow', fps=30)
    print('Gif saved')


def main():
    # filename = 'quakes_2023_6dot5.csv'
    # k = 5
    # repeat = 1000
    k = int(input("Enter the number of clusters: "))
    repeat = int(input("Enter the number of iterations: "))
    raw = input("Enter the data file name: ")
    filepath = raw.split()
    for filep in filepath:
        # data = readData(filep)
        data = get_quake_data(2024, 2)
        data, centroids, isStable = kmeans(data, k, repeat)
        print('Stable' if isStable else 'Unstable')
        for i in range(k):
            print(f'Cluster {i+1}:')
            for d in data:
                if d.cluster == i:
                    print(f'  {d.coor[0]:6.2f}, {d.coor[1]:6.2f}')
            print(f'Centroid: {centroids[i][0]:6.2f}, {centroids[i][1]:6.2f}')

        if isNumpy:
            draw_3Dmap(data, centroids)
        else:
            draw_map(data, centroids)


if __name__ == "__main__":
    main()
