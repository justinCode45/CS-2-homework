from world2 import *


class Fish(Animal):

    def __init__(self) -> None:
        super().__init__()
        self._turtle.shape("fish.gif")

    def liveAlittle(self):
        offset = [(-1, -1), (0, -1), (1, -1),
                  (-1, 0),       (1, 0),
                  (-1, 1), (0, 1), (1, 1)]

        adjFish = 0

        for adj in offset:
            x = self.getX() + adj[0]
            y = self.getY() + adj[1]

            if x >= 0 and x < self._world.getMaxX() and y >= 0 and y < self._world.getMaxY():
                if not self._world.empty(x, y):
                    adjFish += 1

        if adjFish >= 2:
            self._world.delThing(self)

        else:
            self._breedTicks += 1
            if self._breedTicks >= 12:
                self.tryBreed()
            self.tryMove()

    def tryBreed(self):
        nextX = -1
        nextY = -1
        while not (0 <= nextX < self._world.getMaxX() and 0 <= nextY < self._world.getMaxY()):
            offset = [(-1, -1), (0, -1), (1, -1),
                      (-1, 0),       (1, 0),
                      (-1, 1), (0, 1), (1, 1)]

            i = random.randrange(len(offset))
            offset = offset[i]
            nextX = self.getX() + offset[0]
            nextY = self.getY() + offset[1]

        if self._world.empty(nextX, nextY):
            child = Fish()
            self._world.addlife(child, nextX, nextY)
            self._breedTicks = 0

