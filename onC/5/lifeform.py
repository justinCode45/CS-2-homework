import random
import turtle
from world2 import *


class LifeForm:
    def __init__(self) -> None:
        self.__xPos = 0
        self.__yPos = 0
        self.__world = None
        self.__trutle = turtle.Turtle()
        self.__breedTicks = 0
        self.__turtle.up()
        self.__turtle.hideturtle()

    def getX(self):
        return self.__xPos
    
    def getY(self):
        return self.__yPos
    
    def setX(self, x):
        self.__xPos = x

    def setY(self, y):
        self.__yPos = y

    def getWorld(self):
        return self.__world
    
    def getBreedTicks(self):
        return self.__breedTicks

    def imcremenBreedTicks(self):
        self.__breedTicks += 1

    def changeShape(self, shape):
        self.__turtle.shape(shape)

    def appear(self):
        self.__turtle.goto(self.__xPos, self.__yPos)
        self.__turtle.showturtle()

    def hide(self):
        self.__turtle.hideturtle()

    def move(self,_x,_y):
        self.__world.moveLife(self.__xPos, self.__yPos, _x, _y)
        self.__xPos = _x
        self.__yPos = _y
        self.__turtle.goto(self.__xPos, self.__yPos)

    def tryToBreed(self, child):
        offset = [(-1, -1), (0, -1), (1, -1),
                    (-1, 0),       (1, 0),
                    (-1, 1), (0, 1), (1, 1)]
        i = random.randrange(len(offset))
        offset = offset[i]
        newx = self.__xPos + offset[0]
        newy = self.__yPos + offset[1]

        while not(0<= newx < self.__world.getMaxX() and 0 <= newy < self.__world.getMaxY()):
            i = random.randrange(len(offset))
            offset = offset[i]
            newx = self.__xPos + offset[0]
            newy = self.__yPos + offset[1]

        if self.__world.empty(newx, newy):
            aNewthing = child
            self.__world.addLife(aNewthing, newx, newy)
            self.__breedTicks = 0

    
    def tryToMove(self):
        nextX = -1
        nextY = -1
        while not (0 <= nextX < self.__world.getMaxX() and 0 <= nextY < self.__world.getMaxY()):
            offset = [(-1, -1), (0, -1), (1, -1),
                      (-1, 0),       (1, 0),
                      (-1, 1), (0, 1), (1, 1)]
            i = random.randrange(len(offset))
            offset = offset[i]
            nextX = self.getX() + offset[0]
            nextY = self.getY() + offset[1]
        if self.__world.empty(nextX, nextY):
            self.move(nextX, nextY)

    