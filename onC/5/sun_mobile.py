import turtle


class Sun:
    def __init__(self, name, rad, m, dist, ):
        self.__name = name
        self.__radius = rad
        self.__mass = m
        self.__distance = dist
        self.__x = 0
        self.__y = 0
        self.__sTurtle = turtle.Turtle()
        self.__sTurtle.shape("circle")
        self.__sTurtle.color("yellow")

    def getName(self):
        return self.__name

    def getRadius(self):
        return self.__radius

    def getMass(self):
        return self.__mass

    def getTemperature(self):
        return self.__temperature

    def getDistance(self):
        return self.__distance

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

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

    def setDistance(self, dist):
        self.__distance = dist

    def __str__(self):
        return self.__name

    def setTemperature(self, temp):
        self.__temperature = temp

    def setX(self, x):
        self.__x = x

    def setY(self, y):
        self.__y = y