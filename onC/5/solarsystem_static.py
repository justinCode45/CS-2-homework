import turtle

class SolarSystem:
    def __init__(self, width,height):
        self.__theSun = None
        self.__planets = []
        self.__ssTurtle = turtle.Turtle()
        self.__ssTurtle.hideturtle()
        self.__ssScreen = turtle.Screen()
        self.__ssScreen.setworldcoordinates(-width/2,-height/2,width/2,height/2)

    def addPlanet(self, p):
        self.__planets.append(p)
    
    def setSun(self,aSum):
        self.__theSun = aSum

    def showPlanets(self):
        for p in self.__planets:
            print(p)

    def freeze(self):
        self.__ssScreen.exitonclick()