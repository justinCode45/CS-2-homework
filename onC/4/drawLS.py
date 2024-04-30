import turtle

def drawLS(t, instructuins,angle, distance):
    for cmd in instructuins:
        if cmd == 'F':
            t.forward(distance)
        elif cmd == '+':
            t.right(angle)
        elif cmd == '-':
            t.left(angle)
    

w = 600
angle = 60
wn = turtle.Screen()
wn.setworldcoordinates(-10,-10,w+10,w+10)

instructions =["F","F-F++F-F","F-F++F-F-F-F++F-F++F-F++F-F-F-F++F-F"]

t = turtle.Turtle()
for i in range(3):
    distance = w/(3**i)
    t.up()
    t.goto(0,200*i)
    t.down()
    drawLS(t,instructions[i],angle,distance)