# File Name : HW9_112652044.py
# Author : Justin Chen
# Email Address : justin.sc12@nycu.edu.tw
# HW Number : 9
# Description : This program will process image and compress the image using SVD.
# Last Changed : 2024/4/21
# Dependencies : Python 3.12.2, numpy
# Additional :
#   1. SVD compress function is implemented.
#   2. flipX and flipY function is implemented.
#   3. faster
import turtle
import time
import tkinter as tk
from threading import Thread
from turtle import RawTurtle
from tkinter import Canvas, Button

WIDTH = 900
HEIGHT = 900


class LSystem:

    def __init__(self, angle: float, size: float, dim: float, axiom: str, rules: dict[str, str]):
        self.axiom: str = axiom
        self.rules: dict[str, str] = rules
        self.size: float = size
        self.angle: float = angle
        self.dim: float = dim

    def instructions(self, depth: int):
        inst = self.axiom
        length = self.size/(self.dim**depth)
        # length =self.size
        for _ in range(depth):
            inst = ''.join([self.rules.get(c, c) for c in inst])
        for c in inst:
            yield (c, length, self.angle)


class LSCanvasBuffer:

    def __init__(self, root: tk.Tk, system: LSystem, initState: tuple[tuple, int] = ((0, 0), 0)):
        self.root: tk.Tk = root
        self.system: LSystem = system
        self.initState: tuple = initState
        self.buffer: dict[int, Canvas] = {}

    def __getitem__(self, key: int):
        if key not in self.buffer:
            c = Canvas(self.root, width=WIDTH, height=HEIGHT)
            draw_LS(c, self.system, key, self.initState)
            self.buffer[key] = c
        return self.buffer[key]

    def generate(self, depth: int):
        if depth not in self.buffer:
            c = Canvas(self.root, width=WIDTH, height=HEIGHT)
            draw_LS(c, self.system, depth, self.initState)
            self.buffer[depth] = c


def draw_LS(canvas: Canvas, system: LSystem, depth: int, initState: tuple[tuple, int] = ((0, 0), 0)):
    state = []
    t = RawTurtle(canvas)
    t.getscreen().tracer(0)
    t.hideturtle()
    t.setheading(initState[1])
    t.teleport(initState[0][0], initState[0][1])
    for instr in system.instructions(depth):
        c, l, a = instr
        if c == 'F':
            t.forward(l)
        elif c == 'M':
            t.up()
            t.forward(l)
            t.down()
        elif c == '+':
            t.right(a)
        elif c == '-':
            t.left(a)
        elif c == '[':
            state.append((t.position(), t.heading()))
        elif c == ']':
            s = state.pop()
            t.setheading(s[1])
            t.up()
            t.goto(s[0])
            t.down()
    t.getscreen().update()


def animate_LS(fram: LSCanvasBuffer, depth: int, delay=0.5):
    for i in range(depth+1):
        c = fram[i]
        c.pack()
        c.update()
        time.sleep(delay)
        c.pack_forget()
        c.update()


def load_LS(path: str):
    with open(path, 'r') as f:
        angle = float(f.readline())
        size = float(f.readline())
        dim = float(f.readline())
        axiom = f.readline()[:-1]
        rules = {}
        for line in f:
            key, value = line.split()
            rules[key] = value
        return LSystem(angle, size, dim, axiom, rules)


class App:

    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.title("LSystem")
        self.root.geometry(f"{WIDTH+100}x{HEIGHT}")
        # self.btn_ = 
        
    def click(self,event):
        pass


    def run(self):
        self.root.mainloop()

    

def main():
    cantor_set = LSystem(0, 500, 3,
                         '[F]',
                         {'F': 'FMF',
                          'M': 'MMM'})
    koch_curve = LSystem(60, 500, 3,
                         '[F++F++F]',
                         {'F': 'F-F++F-F'})
    rosemary = LSystem(25.7, 350, 2,
                       '[H]',
                       {'H': 'HFX[+H][-H]',
                        'X': 'X[-FFF][+FFF]FX'})
    levy_curve = load_LS("levy_curve.txt")
    root = tk.Tk()
    levyCurve_buffer = LSCanvasBuffer(root, levy_curve, ((-100, -100), 0))
    levyCurve_buffer.generate(16)
    animate_LS(levyCurve_buffer, 16)
    # levyCurve_buffer[10].pack()
    # rosemary_buffer = LSCanvasBuffer(root, rosemary, ((-300, 0), 0))
    # rosemary_buffer.generate(8)
    # for _ in range(2):
    #     animate_LS(rosemary_buffer, 8, 0.5)

    # rosemary_buffer[8].pack()
    levyCurve_buffer[16].pack()
    root.mainloop()


if __name__ == "__main__":
    main()
