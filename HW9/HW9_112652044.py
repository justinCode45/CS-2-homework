# File Name : HW9_112652044.py
# Author : Justin Chen
# Email Address : justin.sc12@nycu.edu.tw
# HW Number : 9
# Description : Show fractal pattern by LSystem, and save the image as .png or .gif
# Last Changed : 2024/5/16
# Dependencies : Python 3.12.2, tkinter, turtle, PIL, ghostscript
# Additional :
#   1. beautiful GUI
#   2. save the image as .png or .gif(needs ghostscript)
#   3. support multiple L-System pattern
#   4. support both draw and animate mode
#   5. support error handling
#   6. support timeout handling
#   7. read L-System from file
# Please install ghostscript and PIL in order to save image

import time
import tkinter as tk
from turtle import RawTurtle
from tkinter import Canvas, Button, messagebox
from PIL import Image, ImageTk
import signal
import traceback
import io
# you can change the following parameters
WIDTH = 800
HEIGHT = 800
# TIMEOUTTIME is the time limit for each show
TIMEOUTTIME = 9
PATTERN = ["cantor_set", "koch_curve",
           "rosemary", "levy_curve", "ring", "crystal"]


class LSystem:
    # LSystem is a class for L-System, it will store the axiom, rules, angle, size, and dim
    # use instructions to generate the instruction for turtle
    def __init__(self, angle: float, size: float, dim: float, axiom: str, rules: dict[str, str]):
        self.axiom: str = axiom
        self.rules: dict[str, str] = rules
        self.size: float = size
        self.angle: float = angle
        self.dim: float = dim

    def instructions(self, depth: int):
        inst = self.axiom
        length = self.size/(self.dim**depth)
        for _ in range(depth):

            inst = ''.join([self.rules.get(c, c) for c in inst])

        for c in inst:
            if c == 'T':
                length *= self.dim
                continue
            elif c == 't':
                length /= self.dim
                continue
            yield (c, length, self.angle)


class LSCanvasBuffer:
    # LSCanvasBuffer is a buffer for LSystem, it will store the canvas for each depth
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
    # draw_LS will draw the L-System pattern on the canvas
    state = []
    t = RawTurtle(canvas)
    t.getscreen().tracer(0)
    t.hideturtle()
    t.pensize(2)
    t.setheading(initState[1])
    t.up()
    t.goto(initState[0])
    t.down()
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
    # animate_LS will animate the L-System pattern on the canvas
    for i in range(depth+1):
        c = fram[i]
        c.pack()
        c.update()
        time.sleep(delay)
        c.pack_forget()
        c.update()


def load_LS(path: str):
    # load_LS will load the L-System from the file
    scaler = HEIGHT/512
    with open(path, 'r') as f:
        init_state = f.readline().split()
        init_state = ((float(init_state[0])*scaler,
                       float(init_state[1])*scaler), float(init_state[2]))
        angle = float(f.readline())
        size = float(f.readline())*scaler
        dim = float(f.readline())
        axiom = f.readline()[:-1]
        rules = {}
        for line in f:
            key, value = line.split()
            rules[key] = value if value != '_' else ''
        return LSystem(angle, size, dim, axiom, rules), init_state


class App:

    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.title("LSystem")
        self.root.geometry(f"{WIDTH+200}x{HEIGHT}")

        self.btn_show: Button = Button(
            self.root, text="Show", command=self.timeout_show)
        self.btn_save: Button = Button(
            self.root, text="Save", command=self.save)
        self.pattern: list[str] = PATTERN
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


        img = Image.open("pic.jpg")
        img.thumbnail((WIDTH, HEIGHT))
        self.img = ImageTk.PhotoImage(img)
        self.pic_label = tk.Label(self.pic_fram, image=self.img)
        

        self.pic_fram.grid(row=0, column=0, rowspan=4)
        self.btn_show.grid(row=3, column=2)
        self.btn_save.grid(row=3, column=3)
        self.menu.grid(row=0, column=2, columnspan=2)
        self.rbtn1.grid(row=1, column=2)
        self.rbtn2.grid(row=1, column=3)
        self.spin_depth.grid(row=2, column=2, columnspan=2)

        self.LSDict: dict[str, LSCanvasBuffer] = {}
        tk.Tk.report_callback_exception = self.show_error

    def show(self):
        for c in self.pic_fram.winfo_children():
            c.pack_forget()
        pattern = self.value_pattern.get()
        depth = self.value_depth.get()
        mode = self.value_mode.get()
        if mode == 0:
            c = self.LSDict[pattern][depth]
            c.pack()
        else:
            lsbuffer = self.LSDict[pattern]
            animate_LS(lsbuffer, depth)
            lsbuffer[depth].pack()

    def rendering(self):
        rendering_lable = tk.Label(
            self.pic_fram, text="Rendering...\nIf it takes too long, please CTRL+C in terminal.")
        for c in self.pic_fram.winfo_children():
            c.pack_forget()
        rendering_lable.pack(expand=True, fill="none")
        pattern = self.value_pattern.get()
        depth = self.value_depth.get()
        mode = self.value_mode.get()
        if mode == 0:
            c = self.LSDict[pattern][depth]
            rendering_lable.pack_forget()
        else:
            lsbuffer = self.LSDict[pattern]
            lsbuffer.generate(depth)
            rendering_lable.pack_forget()

    def heandler(self, *args):
        for c in self.pic_fram.winfo_children():
            c.pack_forget()
        self.pic_label.pack(fill="none", expand=True)
        raise Exception("Timeout")

    def timeout_show(self):
        signal.signal(signal.SIGALRM, self.heandler)
        signal.alarm(TIMEOUTTIME)
        self.rendering()
        signal.alarm(0)
        self.show()

    def show_error(self, *args):
        err = traceback.format_exception(*args)
        messagebox.showerror("Error", err[-1])

    def save(self):
        self.timeout_show()
        pattern = self.value_pattern.get()
        depth = self.value_depth.get()
        mode = self.value_mode.get()
        try:
            if mode == 0:
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
                           append_images=l[1:], duration=len(l)*15, loop=0)
        except:
            print("Please install ghostscript and PIL in order to save image")
            raise Exception(
                "Please install ghostscript and PIL in order to save image")
        extfilename = "gif" if mode else "png"
        messagebox.showinfo("Save",
                            f"Save as {pattern}_{depth}.{extfilename} ")

    def preprocess(self):
        for path in self.pattern:
            try:
                system, initState = load_LS(path+".txt")
                self.LSDict[path] = LSCanvasBuffer(
                    self.pic_fram, system, initState)
            except:
                self.pattern.remove(path)
                print(f"File {path}.txt not found")
                raise Exception(f"File {path}.txt not found")

    def run(self):
        self.root.after(0, self.preprocess)
        self.root.mainloop()


if __name__ == "__main__":
    # main()
    a = App()
    a.run()
