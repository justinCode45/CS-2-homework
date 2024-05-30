import random
import turtle
from world import *
from fish import *
from bear import *


def main():

    numBera = 10
    numFish = 10
    worldTime = 200
    worldWidth = 50
    worldHeight = 25

    myworld = World(worldWidth, worldHeight)
    myworld.draw()

    for _ in range(numFish):
        newFish = Fish()
        x = random.randrange(myworld.getMaxX())
        y = random.randrange(myworld.getMaxY())
        while not myworld.empty(x, y):
            x = random.randrange(myworld.getMaxX())
            y = random.randrange(myworld.getMaxY())
        myworld.addlife(newFish, x, y)

    for _ in range(numBera):
        newBear = Bear()
        x = random.randrange(myworld.getMaxX())
        y = random.randrange(myworld.getMaxY())
        while not myworld.empty(x, y):
            x = random.randrange(myworld.getMaxX())
            y = random.randrange(myworld.getMaxY())
        myworld.addlife(newBear, x, y)

    for t in range(worldTime):
        myworld.liveAlittle()
        print("Time: ", t)
    
    myworld.freeze()

if __name__ == "__main__":
    main()
