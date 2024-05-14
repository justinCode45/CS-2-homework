class Sun:
    def __init__(self, name, rad, m, dist, temp):
        self.__name = name
        self.__radius = rad
        self.__mass = m
        self.__distance = dist
        self.__temperature = temp

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