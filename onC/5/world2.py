import random
import turtle
import time


class Animal:

    def __init__(self) -> None:
        self._x = 0
        self._y = 0
        self._world: 'World' = None
        self._breedTicks = 0
        self._turtle = turtle.Turtle()
        self._turtle.up()
        self._turtle.hideturtle()

    def getX(self):
        return self._x

    def getY(self):
        return self._y

    def setX(self, x):
        self._x = x

    def setY(self, y):
        self._y = y

    def setWorld(self, w):
        self._world = w

    def appear(self):
        self._turtle.goto(self._x, self._y)
        self._turtle.showturtle()

    def hide(self):
        self._turtle.hideturtle()

    def move(self, newX, newY):
        self._world.movelive(self._x, self._y, newX, newY)
        self._x = newX
        self._y = newY
        self._turtle.goto(self._x, self._y)

    def liveAlittle(self):
        pass

    def tryBreed(self):
        pass

    def tryMove(self):
        nextX = -1
        nextY = -1
        while not (0 <= nextX < self._world.getMaxX() and 0 <= nextY < self._world.getMaxY()):
            offset = [(-1, -1), (0, -1), (1, -1),
                      (-1, 0),       (1, 0),
                      (-1, 1), (0, 1), (1, 1)]

            i = random.randrange(len(offset))
            offset = offset[i]
            nextX = self.getX() + offset[0]
            nextY = self.getY() + offset[1]
        if self._world.empty(nextX, nextY):
            self.move(nextX, nextY)
            self.setX(nextX)
            self.setY(nextY)


class World:

    def __init__(self, mx, my) -> None:

        self.__maxX = mx
        self.__maxY = my
        self.__lifeList: list[Animal] = []

        self.__grid = []
        for _ in range(self.__maxY):
            row = [None for _ in range(self.__maxX)]
            self.__grid.append(row)
        self.__wScreen = turtle.Screen()
        self.__wScreen.setworldcoordinates(-1, -1, self.__maxX, self.__maxY)
        self.__wScreen.addshape("bear.gif")
        self.__wScreen.addshape("fish.gif")

        self.__wTurtle = turtle.Turtle()
        self.__wTurtle.hideturtle()

    def draw(self):
        self.__wScreen.tracer(0)
        self.__wTurtle.color("silver")

        for i in range(self.__maxX):
            self.__wTurtle.penup()
            self.__wTurtle.goto(i, 0)
            self.__wTurtle.pendown()
            self.__wTurtle.goto(i, self.__maxY-1)

        for i in range(self.__maxY):
            self.__wTurtle.penup()
            self.__wTurtle.goto(0, i)
            self.__wTurtle.pendown()
            self.__wTurtle.goto(self.__maxX-1, i)

        self.__wTurtle.teleport(0, 0)
        self.__wScreen.tracer(1)

    def addlife(self, life: Animal, x, y):
        life.setX(x)
        life.setY(y)
        self.__grid[y][x] = life
        life.appear()
        life.setWorld(self)
        self.__grid[y][x] = life
        self.__lifeList.append(life)

    def delThing(self, life: Animal):
        x = life.getX()
        y = life.getY()
        self.__grid[y][x] = None
        self.__lifeList.remove(life)

    def movelive(self, x, y, nx, ny):
        self.__grid[ny][nx] = self.__grid[y][x]
        self.__grid[y][x] = None

    def getMaxX(self):
        return self.__maxX

    def getMaxY(self):
        return self.__maxY

    def liveAlittle(self):
        if not self.__lifeList == []:
            a = random.randint(0, len(self.__lifeList)-1)
            self.__lifeList[a].liveAlittle()

    def empty(self, x, y):
        return self.__grid[y][x] == None

    def lookAtLocation(self, x, y):
        return self.__grid[y][x]

    def freeze(self):
        self.__wScreen.exitonclick()
