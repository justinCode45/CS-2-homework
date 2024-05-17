# import hashlib
# import io
# import PIL
# from PIL import Image
# def encrypt(path: str):
#     with open(path, 'rb') as f:
#         data = f.read()
#     key = hashlib.sha256("password".encode()).hexdigest()
#     encrypted_data = bytearray(x ^ ord(key[i % len(key)]) for i, x in enumerate(data))
#     with open(path+"C", 'wb') as f:
#         f.write(encrypted_data)
    
# def decrypt(path: str):
#     with open(path, 'rb') as f:
#         data = f.read()
#     key = hashlib.sha256("password".encode()).hexdigest()
#     decrypted_data = bytearray(x ^ ord(key[i % len(key)]) for i, x in enumerate(data))
#     with open(path+"D", 'wb') as f:
#         f.write(decrypted_data)
#     return decrypted_data

# encrypt("surprise.mygo")
# bimg = decrypt("surprise.mygoC")
# img = Image.open(io.BytesIO(bimg))
# img.show()
# img.save("form.jpg")
# import compileall
from tkinter import Canvas, Button, messagebox, Tk
from PIL import Image, ImageTk
from decimal import Decimal
import turtle
from math import sqrt
from math import pow


M_EARTH = Decimal(5927)*Decimal(10)**Decimal(21)
AU = Decimal(149597870.7)*Decimal(10)**Decimal(3)
SCALE = Decimal(1)*Decimal(10)**Decimal(-3.5)
TIME_SCALE = Decimal(1)*Decimal(10)**Decimal(-1)
G = Decimal(6.67430)*Decimal(10)**Decimal(-11)

class Vec2D:

    def __init__(self, _x: float, _y: Decimal) -> None:
        self.x: Decimal = Decimal(_x)
        self.y: Decimal = Decimal(_y)

    def __add__(self, other: 'Vec2D') -> 'Vec2D':
        return Vec2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other: 'Vec2D') -> 'Vec2D':
        return Vec2D(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Decimal) -> 'Vec2D':
        return Vec2D(self.x * other, self.y * other)

    def __truediv__(self, other: Decimal) -> 'Vec2D':
        return Vec2D(self.x / other, self.y / other)

    def norm(self) -> Decimal:
        return (self.x**2 + self.y**2)**Decimal(0.5)

    

class Planet:

    def __init__(self, _mass: float, _pos: Vec2D, _vel: Vec2D) -> None:
        self.mass = Decimal(_mass)
        self.pos = _pos
        self.vel = _vel


class SolarSystem:

    def __init__(self) -> None:
        self.planets: dict[int,Planet] = {} 
        self.size = 0
        self.G = G

    def addPlanet(self, planet: Planet) -> None:
        self.planets[self.size] = (planet)
        self.size += 1

    def update(self, dt: float) -> None:
        dt = Decimal(dt) * TIME_SCALE
        old_planets = self.planets.copy()
        
        for i in self.planets.keys():
            F =  Vec2D(0,0)
            for j in self.planets.keys():
                if i == j:
                    continue
                r = old_planets[j].pos - old_planets[i].pos
                if r.norm() < 0.0001:
                    continue
                F += r * (self.G * old_planets[i].mass * old_planets[j].mass) / (r.norm()**3)
            
            acc = F / old_planets[i].mass
            self.planets[i].vel += acc * dt
            self.planets[i].pos += self.planets[i].vel * dt
        
        for i in range(len(self.planets)):
            print(f"Planet {i} pos: {self.planets[i].pos.x:.3f} {self.planets[i].pos.y:.3f}")
            print(f"Planet {i} vel: {self.planets[i].vel.x:.3f} {self.planets[i].vel.y:.3f}")
            print()
        print("----------------------------------------------------")

def transform(scale: Decimal, p: Vec2D) -> Vec2D:
    return Vec2D(p.x*scale, p.y*scale) + Vec2D(400, 400)

class App:

    def __init__(self) -> None:
        self.system = SolarSystem()
        self.root = Tk()
        self.root.title("Solar System")
        self.root.geometry("800x800")
        self.canvas = Canvas(self.root, width=800, height=800)
        self.canvas_obj: dict = {}

    def update(self) -> None:
        dt = 1
        self.system.update(dt)

        self.canvas.delete("line")
        for key in self.system.planets.keys():
            pos = transform(SCALE, self.system.planets[key].pos)
            self.canvas.moveto(self.canvas_obj[key], pos.x, pos.y)
        
        for p in self.system.planets.keys():
            #draw vel
            print(p)
            p = self.system.planets[p]
            pos = transform(SCALE, p.pos)
            vel =  p.vel * SCALE *  100
            print(vel.x, vel.y)
            self.canvas.create_line(pos.x, pos.y, pos.x+vel.x, pos.y+vel.y, fill="red", tags="line")

        self.root.after(dt, self.update)

    def run(self) -> None:
        self.root.after(1, self.update)

        for key in self.system.planets.keys():
            pos = transform(SCALE, self.system.planets[key].pos)
            b = self.canvas.create_oval(float(pos.x)-1.5, float(pos.y)-1.5,
                                        float(pos.x)+1.5, float(pos.y)+1.5, fill="blue")
            self.canvas_obj[key] = b
        
        self.canvas.pack()
        self.root.mainloop()
    
    def addPlanet(self, planet: Planet) -> None:
        self.system.addPlanet(planet)




if __name__ == "__main__":
    
    # sun = Planet(Decimal(333000)*M_EARTH, Vec2D(0, 0), Vec2D(0, 0))
    earth = Planet(M_EARTH, Vec2D(0, 0), Vec2D(0, 0))
    moon = Planet(Decimal(0.0123)*M_EARTH, Vec2D(405696, 0), Vec2D(0, 1.2*sqrt(G*M_EARTH/Decimal(405696))))
    print(sqrt(G*M_EARTH/Decimal(405696)))
    t = 29.5*24*60*60
    t * sqrt(G*M_EARTH) * 2 * 3.14159
    exit(0)
    app = App()
    # app.addPlanet(sun)
    app.addPlanet(moon)
    app.addPlanet(earth)
    app.run()