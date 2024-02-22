import turtle

def drawTriangle(t: turtle.Turtle, sz):
    for length in range(1,sz,5):
        t.forward(length)
        t.left(120)

t = turtle.Turtle()
drawTriangle(t, 100)