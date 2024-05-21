# Addtional funtinon:
#   1. There is no any turtle get hurt in this code.

from tkinter import Canvas, Tk, Label, ALL
from PIL import Image, ImageTk
from decimal import Decimal as Dec
from threading import Thread
import tkinter as tk

M_EARTH = Dec(5927)*Dec(10)**Dec(21)
AU = Dec(149597870.7)*Dec(10)**Dec(3)
DIS_SCALE = Dec(1)*Dec(10)**Dec(-9.5)
TIME_SCALE = Dec(1)*Dec(10)**Dec(3.5)
G = Dec(6.67430)*Dec(10)**Dec(-11)
M_SUN = Dec(333000)*M_EARTH


class Vec2D:

    def __init__(self, _x: float, _y: Dec) -> None:
        self.x: Dec = Dec(_x)
        self.y: Dec = Dec(_y)

    def __add__(self, other: 'Vec2D') -> 'Vec2D':
        return Vec2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other: 'Vec2D') -> 'Vec2D':
        return Vec2D(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Dec) -> 'Vec2D':
        return Vec2D(self.x * other, self.y * other)

    def __truediv__(self, other: Dec) -> 'Vec2D':
        return Vec2D(self.x / other, self.y / other)

    def norm(self) -> Dec:
        return (self.x**2 + self.y**2)**Dec(0.5)


class Planet:

    def __init__(self, _mass: float, _pos: Vec2D, _vel: Vec2D) -> None:
        self.mass = Dec(_mass)
        self.pos = _pos
        self.vel = _vel
        self.img = None
        self.isfixed = False
        self.name = ""

    def config(self, **data) -> None:

        for key in data:
            self.__dict__[key] = data[key]


class SolarSystem:

    def __init__(self) -> None:
        self.planets: dict[int, Planet] = {}
        self.size = 0
        self.G = G

    def addPlanet(self, planet: Planet) -> None:
        self.planets[self.size] = (planet)
        self.size += 1

    def update(self, dt: float, timescale) -> None:
        dt = Dec(dt) * timescale
        old_planets = self.planets.copy()

        for i in self.planets.keys():
            if self.planets[i].isfixed:
                continue
            F = Vec2D(0, 0)
            for j in self.planets.keys():
                if i == j:
                    continue
                r = old_planets[j].pos - old_planets[i].pos
                if r.norm() < 0.0001:
                    continue
                f = r * (self.G * old_planets[i].mass * old_planets[j].mass)
                f /= (r.norm()**3)
                F += f

            acc = F / old_planets[i].mass
            self.planets[i].vel += acc * dt
            self.planets[i].pos += self.planets[i].vel * dt


class Path:

    size = -1

    def __init__(self, c):
        self.path = []
        self.canvas: Canvas = c

    @classmethod
    def csize(cls):
        if cls.size == -1:
            cls.size = 200
        else:
            cls.size = -1

    def add(self, p):
        self.path.append(p)
        if self.size == -1:
            return
        while len(self.path) > self.size:
            p = self.path.pop(0)
            self.canvas.delete(p)

    def clear(self):
        for p in self.path:
            self.canvas.delete(p)


class App:

    def __init__(self, _system) -> None:
        self.root = Tk()
        self.root.title("Solar System")
        self.root.geometry(f"{800}x{800+100}")

        self.universe = Canvas(self.root, width=1000, height=1000, bg="#040310")
        self.time_var = tk.DoubleVar()
        self.time_lable = Label(self.root, textvariable=self.time_var,
                                font=("TkFixedFont", 16), anchor="w", bg="white")
        self.time_var.set(0)

        self.system: SolarSystem = _system
        self.uplanet: dict = {}
        self.uPimgae: dict = {}
        self.upath: dict[int, Path] = {}

        self.universe.bind("<ButtonPress-1>", self.scroll_start)
        self.universe.bind("<B1-Motion>", self.scroll_move)
        self.universe.bind("<Button-4>", self.zoomerP)
        self.universe.bind("<Button-5>", self.zoomerM)

        for i in range(len(self.system.planets.keys())):
            self.universe.bind(f"{i+1}", lambda event,
                               i=i: self.focus(event, i))

        self.universe.bind("z", lambda event: self.time_scale_change(event, 1))
        self.universe.bind("x", lambda event: self.time_scale_change(event, 2))
        self.universe.bind("c", lambda event: self.time_scale_change(event, 3))
        self.universe.bind(
            "<space>", lambda event: self.time_scale_change(event, 4))
        self.universe.bind("a", lambda event: Path.csize())

        self.universe.focus_set()
        self.timescale = TIME_SCALE

        self.disscale = DIS_SCALE
        self.translate = Vec2D(400, 400)

        self.planetsize = 0.05
        self.mouse = Vec2D(0, 0)

    def time_scale_change(self, event, i):
        # change the time scale
        if i == 1:
            self.timescale = TIME_SCALE
        elif i == 2:
            self.timescale = TIME_SCALE*10
        elif i == 3:
            self.timescale = TIME_SCALE*100
        elif i == 4:
            self.timescale = 0

    def transform(self, p: Vec2D) -> Vec2D:
        # change the coordinate system
        return Vec2D(p.x*self.disscale, p.y*self.disscale)+self.translate

    def focus(self, event, i):
        # foucus on the planet
        canvas_center = self.universe.coords(self.uplanet[i])

        view_center = (self.universe.canvasx(870/2),
                       self.universe.canvasy(870/2))

        translate = (view_center[0] - canvas_center[0],
                     view_center[1] - canvas_center[1])
        self.translate += Vec2D(translate[0], translate[1])

        self.universe.move(ALL, translate[0], translate[1])

    def update(self) -> None:
        # main loop
        dt = 1

        if len(self.uplanet) == 0:
            self.root.after(1, self.update)
            return

        p = [self.universe.coords(self.uplanet[key])
             for key in self.system.planets.keys()]
        self.system.update(dt, self.timescale)

        self.time_var.set(self.time_var.get() + dt *
                          float(self.timescale)/(60*60*24*365))

        for key in self.system.planets.keys():
            pos = self.transform(self.system.planets[key].pos)

            self.universe.moveto(self.uplanet[key],
                                 float(pos.x)-self.planetsize, float(pos.y)-self.planetsize)

            line = self.universe.create_line(
                p[key][0]+self.planetsize, p[key][1]+self.planetsize, 
                float(pos.x), float(pos.y), fill="red")
            self.upath[key].add(line)

        self.universe.update()
        self.root.after(dt, self.update)

    def run(self) -> None:
        # preprocess
        self.root.after(1, self.update)
        self.time_lable.pack(expand=True, fill="x")

        for key in self.system.planets.keys():
            pos = self.transform(self.system.planets[key].pos)

            b = self.universe.create_oval(float(pos.x)-self.planetsize, float(pos.y)-self.planetsize,
                                          float(pos.x)+self.planetsize, float(pos.y)+self.planetsize, fill="blue")
            self.uplanet[key] = b
            self.upath[key] = Path(self.universe)

        self.universe.pack()

        self.root.mainloop()

    def scroll_start(self, event):
        # drag the canvas
        self.mouse = Vec2D(event.x, event.y)

    def scroll_move(self, event):
        # drag the canvas
        translat = Vec2D(event.x, event.y) - self.mouse
        self.universe.move(ALL, translat.x, translat.y)
        self.translate += translat
        self.mouse = Vec2D(event.x, event.y)

    def zoomerP(self, event):
        # zoom in
        self.mouse = Vec2D(event.x, event.y)
        self.mouse = (self.universe.canvasx(event.x), self.universe.canvasy(event.y))
        self.disscale *= Dec(1.1)
        self.planetsize *= 1.1
        self.universe.delete(ALL)

        for key in self.system.planets.keys():
            p = self.system.planets[key]
            pos = self.transform(p.pos)
            if self.planetsize >= 1 and p.img:
                img = Image.open(p.img)
                img = img.resize((int(2*self.planetsize), int(2*self.planetsize)))
                img = ImageTk.PhotoImage(img)
                self.uplanet[key] = self.universe.create_image(
                    float(pos.x) - self.planetsize, float(pos.y) - self.planetsize, image=img, anchor="nw")
                self.uPimgae[key] = img
            else :
                self.uplanet[key] = self.universe.create_oval(
                    float(pos.x) - self.planetsize, float(pos.y) - self.planetsize, 
                    float(pos.x) + self.planetsize, float(pos.y) + self.planetsize, 
                    fill="blue")

        self.translate = Vec2D(0,0)
        self.root.after(10, self.clear_path)

    def zoomerM(self, event):
        # zoom out
        self.mouse = Vec2D(event.x, event.y)
        self.mouse = (self.universe.canvasx(event.x), self.universe.canvasy(event.y))
        self.disscale *= Dec(0.9)
        self.planetsize *= 0.9 
        self.universe.delete(ALL)

        for key in self.system.planets.keys():
            p = self.system.planets[key]
            pos = self.transform(p.pos)
            if self.planetsize >= 1 and p.img:
                img = Image.open(p.img)
                img = img.resize((int(2*self.planetsize), int(2*self.planetsize)))
                img = ImageTk.PhotoImage(img)
                self.uplanet[key] = self.universe.create_image(
                    float(pos.x) - self.planetsize, float(pos.y) - self.planetsize, image=img, anchor="nw")
                self.uPimgae[key] = img
            else :
                self.uplanet[key] = self.universe.create_oval(
                    float(pos.x) - self.planetsize, float(pos.y) - self.planetsize, 
                    float(pos.x) + self.planetsize, float(pos.y) + self.planetsize, 
                    fill="blue")

        self.translate = Vec2D(0,0)
        self.root.after(10, self.clear_path)

    def clear_path(self):
        for path in self.upath.keys():
            self.upath[path].clear()


def speed(r: Dec, m: Dec) -> Dec:
    # calculate the speed of the planet
    return (G*m/r)**Dec(0.5)


if __name__ == "__main__":

    sun = Planet(M_SUN, Vec2D(0, 0), Vec2D(0, 0))

    earth = Planet(M_EARTH, Vec2D(AU*Dec(1.01673), 0), Vec2D(0, 29783))

    moon = Planet(Dec(0.0123)*M_EARTH,
                  Vec2D(AU*Dec(1.01673)+405696000, 0), Vec2D(0, 29783+1022))

    murcury = Planet(Dec(0.0553)*M_EARTH,
                     Vec2D(AU*Dec(0.466697), 0), Vec2D(0, 47362))

    venus = Planet(Dec(0.815)*M_EARTH,
                   Vec2D(AU*Dec(0.728213), 0), Vec2D(0, 35020))

    mars = Planet(Dec(0.107)*M_EARTH,
                  Vec2D(AU*Dec(1.6666), 0), Vec2D(0, 24077))

    jupiter = Planet(Dec(317.8)*M_EARTH,
                     Vec2D(AU*Dec(5.4588), 0), Vec2D(0, 13070))

    sun.isfixed = True
    earth.vel = Vec2D(0, speed(AU*Dec(1.01673), M_SUN))
    murcury.vel = Vec2D(0, speed(AU*Dec(0.466697), M_SUN))
    venus.vel = Vec2D(0, speed(AU*Dec(0.728213), M_SUN))
    mars.vel = Vec2D(0, speed(AU*Dec(1.6666), M_SUN))
    jupiter.vel = Vec2D(0, speed(AU*Dec(5.4588), M_SUN))
    moon.vel = earth.vel + Vec2D(0, 1022)

    sun.config(name="Sun", img="sun.png")
    earth.config(name="Earth", img="earth.png")
    moon.config(name="Moon", img="moon.png")

    system = SolarSystem()
    system.addPlanet(sun)
    system.addPlanet(murcury)
    system.addPlanet(venus)
    system.addPlanet(earth)
    system.addPlanet(moon)
    system.addPlanet(mars)
    system.addPlanet(jupiter)

    app = App(system)
    app.run()
