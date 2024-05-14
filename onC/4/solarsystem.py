class SolarSystem:

    def __init__(self, s):
        self.__theSun = s
        self.__planets = []

    def addPlanet(self, p):
        self.__planets.append(p)

    def showPlanets(self):
        for p in self.__planets:
            print(p)
