from sun_mobile import *
from planetclass_mobile import *
from solarsystem_mobile import *

def createSSandAnimate():
    ss = SolarSystem(2, 2)
    sun = Sun('SUN', 5000, 10, 5800)
    ss.addSun(sun)

    p = Planet('MERCURY', 19.5, 1000, 0.25, 'blue', 0, 2.0)
    ss.addPlanet(p)

    p = Planet('EARTH', 47.5, 5000, 0.30, 'green', 0, 2.0)
    ss.addPlanet(p)

    p = Planet('MARS', 50, 9000, 0.5, 'red', 0, 1.63)
    ss.addPlanet(p)

    p = Planet('JUPITER', 100, 49000, 0.7, 'black', 0, 1)
    ss.addPlanet(p)

    numTimePeriods = 500
    for aMove in range(numTimePeriods):
        ss.movePlanets()

    ss.freeze()

createSSandAnimate()