from world import *
from fish import *

class Bear(Animal):

    def __init__(self) -> None:
        super().__init__()
        self.__straveTicks = 0
        self._turtle.shape("bear.gif")

    def liveAlittle(self):
        self.__straveTicks += 1
        if self._breedTicks >= 8:
            self.tryBreed()
        
        self.tryEat()
        if self.__straveTicks ==10:
            self._world.delThing(self)
        else:
            self.tryMove()
    
    def tryEat(self):
        offset = [(-1, -1), (0, -1), (1, -1),
                  (-1, 0),       (1, 0),
                  (-1, 1), (0, 1), (1, 1)]

        plist = []
        for adj in offset:
            x = self.getX() + adj[0]
            y = self.getY() + adj[1]

            if x >= 0 and x < self._world.getMaxX() and y >= 0 and y < self._world.getMaxY():
                if not self._world.empty(x, y):
                    thing = self._world.lookAtLocation(x, y)
                    if isinstance(thing, Fish):
                        plist.append(thing)
        
        if len(plist) > 0:
            victim = plist[random.randrange(len(plist))]
            self.move(victim.getX(), victim.getY())
            self._world.delThing(victim)
            self.__straveTicks = 0
        else:
            self.__straveTicks += 1


