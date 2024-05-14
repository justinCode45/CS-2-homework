from planetclass import *

myPlanet = Planet("X25",45,198,100)
print(myPlanet)

print()

print("--Tesst accessor methods--")
n = myPlanet.getName()
print(n)
r = myPlanet.getRadius()
print(r)
m = myPlanet.getMass()
print(m)
d = myPlanet.getDistance()
print(d)


print("--Radius and mass--")
print("Volume: ", myPlanet.getVolume())
print("Surface Area: ", myPlanet.getsurfaceArea())

print("--Density--")
print("Density: ", myPlanet.getDensity())

print("--Test mutator methods--")
myPlanet.setName("X25")
myPlanet.setRadius(45)
myPlanet.setMass(198)
myPlanet.setDistance(100)
print(myPlanet.getName())
print(myPlanet.getRadius())
print(myPlanet.getMass())
print(myPlanet.getDistance())


myhome = Planet("Earth", 6371, 5.97219, 149.6)
print(myhome.getName())
