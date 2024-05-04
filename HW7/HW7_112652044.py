# File Name : HW7_112652044.py
# Author : Justin Chen
# Email Address : justin.sc12@nycu.edu.tw
# HW Number : 7
# Description : This program will process earthquake data and cluster the data using k-means algorithm.
# Last Changed : 2024/5/4
# Dependencies : Python 3.12.2 
# Additional :
#   1. draw a map
#   2. use GCD to calculate distance
#   3. click to show the closest cluster and average magnitude
#   4. load data from web


from math import acos, sin, cos, radians
from csv import reader
from random import sample
import turtle
from urllib import request


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
        data = [Data([float(row[latindex]), float(row[lonindex])], dict(zip(header, row)))
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
    data = [Data([float(row[latindex]), float(row[lonindex])], dict(zip(header, row)))
            for row in datareader]
    return data


def printCluster(data: list[Data], centroids: list[Vec]):
    for i in range(len(centroids)):
        print(f'Cluster {i+1}:')
        print(
            f'+----Centroid: ({centroids[i][0]:6.2f}, {centroids[i][1]:6.2f})')
        for d in data:
            if d.cluster == i:
                print(f'|    | ({d.coor[0]:6.2f}, {d.coor[1]:6.2f})')


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
        # output the result
        print("\033[33mIteration\033[0m", ii+1)
        printCluster(datalist, centroids)

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
    clusteravageMag = [0 for _ in range(len(centroids))]
    clustersize = [0 for _ in range(len(centroids))]
    for d in data:
        t.penup()
        t.goto(d.coor[1], d.coor[0])
        t.pendown()
        t.dot(5, color(d.cluster))
        clusteravageMag[d.cluster] += float(d.info['mag'])
        clustersize[d.cluster] += 1
    clusteravageMag = [clusteravageMag[i] / clustersize[i] if clustersize[i] != 0 else 0
                       for i in range(len(centroids))]
    wn.update()
    p = Vec([0, 0])

    def click(x, y):
        nonlocal p
        p = Vec([y, x])
        print(f"Clicked at ({y:.2f}, {x:.2f})")
        wn.bye()
    wn.onclick(click)
    wn.mainloop()
    c = min(range(len(centroids)), key=lambda i: GCD(p, centroids[i]))
    print(f"Closest cluster: {c+1}")
    print(f"Average magnitude: {clusteravageMag[c]:.2f}")
    turtle.TurtleScreen._RUNNING = True


def main():

    print("Click to show the closest cluster and average magnitude.")
    k = int(input("Enter the number of clusters(<10): "))
    repeat = int(input("Enter the number of iterations: "))
    raw = input(
        "Enter the data file name,split with space(Eenter '0' to load data from web): ")
    filepath = raw.split()
    for filep in filepath:
        data = readData(filep) if filep != '0' else get_quake_data(2024, 10)
        print(f"{"="*10} {filep} {"="*10}")
        data, centroids, isStable = kmeans(data, k, repeat)
        print("\033[32mFinal Result\033[0m")
        print("\033[96m"+('Stable' if isStable else 'Unstable')+"\033[0m")
        printCluster(data, centroids)
        print(f"{"="*10} {filep} {"="*10}")
        draw_map(data, centroids)
        input("\033[37mPress Enter to continue...\033[0m")


if __name__ == "__main__":
    main()
