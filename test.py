import turtle
class Vec2D:
    def __init__(self, _x: float, _y: float):
        self.x = _x
        self.y = _y
    def __add__(self, other: 'Vec2D') -> 'Vec2D':
        return Vec2D(self.x + other.x, self.y + other.y)
    def __sub__(self, other: 'Vec2D') -> 'Vec2D':
        return Vec2D(self.x - other.x, self.y - other.y)
    
    def __mul__(self, other: float) -> 'Vec2D':
        return Vec2D(self.x * other, self.y * other)
    
    def __truediv__(self, other: float) -> 'Vec2D':
        return Vec2D(self.x / other, self.y / other)
    
    def norm(self) -> float:
        return (self.x**2 + self.y**2)**0.5
class Plantes:
    def __init__(self):
        self.mass: float
        self.pos:Vec2D
        self.vel:Vec2D 

class System(Plantes):

    def __init__(self):
        self.planets: list[System] = []
        self.G
    
    def updata(self):
        for planet in self.planets:
            r = planet.pos - self.pos
            F = -self.G * self.mass * planet.mass / r.norm()**3 * r
            acc = F / planet.mass
            dt = 10
            planet.vel += acc * dt
            planet.pos += planet.vel * dt
            planet.updata()


sun = System()
mars = System()
sun.planets.append(mars)
earth = System()
sun.planets.append(earth)
moon = System()
earth.planets.append(moon)



for _ in range(100):
    sun.updata()
    for p in sun.planets:
        realpos = p.pos
        # draw a Plants
        for s in p.planets:
            realpos = s.pos + p.pos

            pass





