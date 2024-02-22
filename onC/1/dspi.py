import turtle

def drawSpiral (t:turtle.Turtle, maxSideLen:float):
    for length in range(1, maxSideLen+1, 5):
        t.forward(length)
        t.right(90)


t = turtle.Turtle()
drawSpiral(t, 100)