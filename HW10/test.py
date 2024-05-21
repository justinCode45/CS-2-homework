import tkinter as tk
from PIL import Image, ImageTk
import turtle
from tkinter import Canvas, Tk, Label, ALL



class app:

    def __init__(self):

        
        self.root = tk.Tk()
        self.universe = Canvas(self.root, width=1000, height=1000, bg="white")
        self.circle = self.universe.create_oval(-50, -50, 50, 50, fill="yellow")
        self.r = self.universe.create_oval(100, 100, 150, 150, fill="yellow")
        self.universe.bind("<ButtonPress-1>", self.scroll_start)
        self.universe.bind("<B1-Motion>", self.scroll_move)
        # self.universe.bind("<Button-4>", self.zoomerP)
        # self.universe.bind("<Button-5>", self.zoomerM)
        # self.universe.focus_set()
        # self.t = turtle.RawTurtle(self.universe)
        # self.t.shape("circle")
        # self.universe.create_oval(100, 100, 200, 200, fill="yellow")
        self.universe.bind("<Button-1>", self.click)
        

    def click(self, event):
        print("_______________________________-")
        print(event.x, event.y)
        print(self.universe.coords(self.circle))
        print(self.universe.canvasx(event.x), self.universe.canvasy(event.y))

    def scroll_start(self, event):
        self.universe.scan_mark(event.x, event.y)
    
    def scroll_move(self, event):
        # self.universe.scan_dragto(event.x, event.y, gain=1)
        
        self.universe.xview_scroll(-1,"units")
        
    def mainloop(self):
        self.universe.create_line(-50+50,-50+50, 400, 400)
        self.universe.moveto(self.circle, 400-50, 400-50)

    def zoomerP(self, event):
        self.universe.scale(ALL, event.x, event.y, 1.1, 1.1)

    def zoomerM(self, event):
        self.universe.scale(ALL, event.x, event.y, 0.9, 0.9)
    def run(self):
        self.universe.pack()
        self.root.after(0, self.mainloop)
        self.root.mainloop()

a = app()
a.run()
