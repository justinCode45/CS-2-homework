import turtle


def drawSquare(t, sz): 
    for i in range(4):
        t.forward(sz)
        t.left(90)
    
def nestedBox(t,sidelength):
    if sidelength >=1:
        drawSquare(t,sidelength)
        nestedBox(t,sidelength-5)
    else:
        return
    
t = turtle.Turtle()
nestedBox(t,100)
t.hideturtle()
turtle.mainloop()