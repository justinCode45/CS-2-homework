import turtle


class Planet:
    def __init__(self, name, rad, m, dist, ic):
        self.__name = name
        self.__radius = rad
        self.__mass = m
        self.__distance = dist
        self.__x = self.__distance
        self.__y = 0
        self.color = ic
        self.__pTurtle = turtle.Turtle()
        self.__pTurtle.shape("circle")
        self.__pTurtle.color(self.color)
        self.__pTurtle.up()
        self.__pTurtle.goto(self.__x, self.__y)
        self.__pTurtle.down()

    def getName(self):
        return self.__name

    def getRadius(self):
        return self.__radius

    def getMass(self):
        return self.__mass

    def getDistance(self):
        return self.__distance

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def getColor(self):
        return self.color

    def getVolume(self):
        return (4/3)*3.14159*(self.__radius**3)

    def getsurfaceArea(self):
        return 4*3.14159*(self.__radius**2)

    def getDensity(self):
        return self.__mass/self.getVolume()

    def setName(self, name):
        self.__name = name

    def setRadius(self, rad):
        self.__radius = rad

    def setMass(self, m):
        self.__mass = m

    def setX(self, x):
        self.__x = x

    def setY(self, y):
        self.__y = y

    def setColor(self, ic):
        self.color = ic

    def setDistance(self, dist):
        self.__distance = dist

    def __str__(self):
        return self.__name
