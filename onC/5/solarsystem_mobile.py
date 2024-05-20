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
    
    def addSun(self,aSum):
        self.__theSun = aSum

    def showPlanets(self):
        for p in self.__planets:
            print(p)

    def movePlanets(self):
        import math
        G =0.1
        dt = 0.01
        for p in self.__planets:
            p.moveto(p.getX() + p.getVelx()*dt, p.getY() + p.getVely()*dt)
            rx = self.__theSun.getX() - p.getX()
            ry = self.__theSun.getY() - p.getY()
            r = math.sqrt(rx**2 + ry**2)
            accx = G*self.__theSun.getMass()*rx/r**3
            accy = G*self.__theSun.getMass()*ry/r**3

            p.setVelx(p.getVelx() + accx*dt)
            p.setVely(p.getVely() + accy*dt)
        
    def freeze(self):
        self.__ssScreen.exitonclick()