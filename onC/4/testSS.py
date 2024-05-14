from planetclass import *
from sun import *
from solarsystem import *


sun = Sun("Sun", 696340, 1.989*(10**30), 0, 5778)
ss = SolarSystem(sun)


p = Planet("Mercury", 2439.7, 3.285*(10**23), 57.9)
ss.addPlanet(p)

p = Planet("Venus", 6051.8, 4.867*(10**24), 108.2)
ss.addPlanet(p)

p = Planet("Earth", 6371, 5.972*(10**24), 149.6)
ss.addPlanet(p)

ss.showPlanets()