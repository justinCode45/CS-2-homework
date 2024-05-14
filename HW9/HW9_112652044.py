# File Name : HW9_112652044.py
# Author : Justin Chen
# Email Address : justin.sc12@nycu.edu.tw
# HW Number : 9
# Description : This program will process image and compress the image using SVD.
# Last Changed : 2024/5/12
# Dependencies : Python 3.12.2, tkinter, turtle, PIL, ghostscript
# Additional :
#   1. beautiful GUI
#   2. save the image as .png or .gif
#   3. support multiple LSystem pattern
#   4. support both draw and animate mode
# Please install ghostscript and PIL in order to save image

import time
import tkinter as tk
from turtle import RawTurtle
from tkinter import Canvas, Button
from PIL import Image
import io

WIDTH = 512
HEIGHT = 512


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
        inst.replace('_', '')
        for c in inst:
            if c == 'T':
                length *= self.dim
                continue
            elif c == 't':
                length /= self.dim
                continue
            yield (c, length, self.angle)


class LSCanvasBuffer:

    def __init__(self, root: tk.Tk, system: LSystem, initState: tuple[tuple, int] = ((0, 0), 0)):
        self.root: tk.Tk = root
        self.system: LSystem = system
        self.initState: tuple = initState
        self.buffer: dict[int, Canvas] = {}

    def __getitem__(self, key: int) -> Canvas:
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


def animate_LS(fram: LSCanvasBuffer, depth: int, delay=0.3):
    for i in range(depth+1):
        c = fram[i]
        c.pack()
        c.update()
        time.sleep(delay)
        c.pack_forget()
        c.update()


def load_LS(path: str):
    with open(path, 'r') as f:
        init_state = f.readline().split()
        init_state = ((float(init_state[0]), float(
            init_state[1])), float(init_state[2]))
        angle = float(f.readline())
        size = float(f.readline())
        dim = float(f.readline())
        axiom = f.readline()[:-1]
        rules = {}
        for line in f:
            key, value = line.split()
            rules[key] = value
        return LSystem(angle, size, dim, axiom, rules), init_state


class App:

    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.title("LSystem")
        self.root.geometry(f"{WIDTH+200}x{HEIGHT}")

        self.btn_show: Button = Button(
            self.root, text="Show", command=self.show)
        self.btn_save: Button = Button(
            self.root, text="Save", command=self.save)
        self.pattern: list[str] = ["cantor_set","penrose",
                                   "koch_curve", "rosemary", "levy_curve"]
        self.value_mode: tk.IntVar = tk.IntVar()
        self.value_pattern: tk.StringVar = tk.StringVar()
        self.menu: tk.OptionMenu = tk.OptionMenu(
            self.root, self.value_pattern, *self.pattern)

        self.rbtn1: tk.Radiobutton = tk.Radiobutton(
            self.root, text="Draw", variable=self.value_mode, value=0)
        self.rbtn2: tk.Radiobutton = tk.Radiobutton(
            self.root, text="Animate", variable=self.value_mode, value=1)

        self.value_depth: tk.IntVar = tk.IntVar()
        self.spin_depth: tk.Spinbox = tk.Spinbox(
            self.root, from_=0, to=50, textvariable=self.value_depth)

        self.value_pattern.set(self.pattern[0])
        self.rbtn1.select()
        self.value_depth.set(0)
        self.pic_fram: tk.Frame = tk.Frame(
            self.root, width=WIDTH, height=HEIGHT)
        self.pic_fram.pack_propagate(False)

        self.pic_fram.grid(row=0, column=0, rowspan=4)
        self.btn_show.grid(row=3, column=2)
        self.btn_save.grid(row=3, column=3)
        self.menu.grid(row=0, column=2, columnspan=2)
        self.rbtn1.grid(row=1, column=2)
        self.rbtn2.grid(row=1, column=3)
        self.spin_depth.grid(row=2, column=2, columnspan=2)

        self.LSDict: dict[str, LSCanvasBuffer] = {}
        try:
            for path in self.pattern:
                system, initState = load_LS(path+".txt")
                self.LSDict[path] = LSCanvasBuffer(
                    self.pic_fram, system, initState)
        except FileNotFoundError:
            print("Please make sure the file exists.")

    def show(self):
        rending_lable = tk.Label(
            self.pic_fram, text="Rending...\nIf it takes too long, please CTRL+C.")
        for c in self.pic_fram.winfo_children():
            c.pack_forget()
        pattern = self.value_pattern.get()
        depth = self.value_depth.get()
        mode = self.value_mode.get()
        if mode == 0:
            rending_lable.pack(expand=True, fill="none")
            c = self.LSDict[pattern][depth]
            rending_lable.pack_forget()
            c.pack()
        else:
            lsbuffer = self.LSDict[pattern]
            rending_lable.pack(expand=True, fill="none")
            lsbuffer.generate(depth)
            rending_lable.pack_forget()
            animate_LS(lsbuffer, depth)
            lsbuffer[depth].pack()

    def save(self):
        self.show()
        pattern = self.value_pattern.get()
        depth = self.value_depth.get()
        if self.value_mode.get() == 0:
            ps = self.LSDict[pattern][depth]
            ps.update()
            ps = ps.postscript()
            image = Image.open(io.BytesIO(ps.encode('utf-8')))
            image.save(f"{pattern}_{depth}.png")
        else:
            l = []
            for i in range(depth+1):
                ps = self.LSDict[pattern][i]
                ps.update()
                ps = ps.postscript()
                image = Image.open(io.BytesIO(ps.encode('utf-8')))
                l.append(image)
            image.save(f"{pattern}_{i}.gif", save_all=True,
                       append_images=l[1:], duration=100, loop=0)

    def run(self):
        self.root.mainloop()


def test():
    cantor_set = LSystem(90, 450, 3,
                         '[F]X',
                         {'F': 'FMF',
                          'M': 'MMM',
                          'X': '-ttMTT+T[F]X'})
    koch_curve = LSystem(60, 250, 3,
                         '[F++F++F]',
                         {'F': 'F-F++F-F'})
    rosemary = LSystem(25.7, 175, 2,
                       '[H]',
                       {'H': 'HFX[+H][-H]',
                        'X': 'X[-FFF][+FFF]FX'})
    levy_curve = load_LS("levy_curve.txt")
    root = tk.Tk()
    cantor_buffer = LSCanvasBuffer(root, cantor_set, ((-225, -64), 0))
    cantor_buffer.generate(5)
    # while 1:
    #     animate_LS(cantor_buffer, 10, 0.5)
    cantor_buffer[5].pack()
    # levyCurve_buffer = LSCanvasBuffer(root, levy_curve, ((-100, -100), 0))
    # levyCurve_buffer.generate(16)
    # animate_LS(levyCurve_buffer, 16)
    # levyCurve_buffer[10].pack()
    # rosemary_buffer = LSCanvasBuffer(root, rosemary, ((-300, 0), 0))
    # rosemary_buffer.generate(8)
    # for _ in range(2):
    #     animate_LS(rosemary_buffer, 8, 0.5)

    # rosemary_buffer[8].pack()
    # levyCurve_buffer[16].pack()
    root.mainloop()


if __name__ == "__main__":
    # main()
    a = App()
    a.run()
