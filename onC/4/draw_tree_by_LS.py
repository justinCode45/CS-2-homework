import turtle

def applyProduction(axiom: str, rules: dict[str, str], n: int):
    for i in range(n):
        newAxiom = ""
        for ch in axiom:
            newAxiom += rules.get(ch,ch)
        axiom = newAxiom
    return axiom


def drawLSystem(t: turtle.Turtle, instructions: str, angle: float, distance: float):
    state = []
    for cmd in instructions:
        if cmd == "F":
            t.forward(distance)
        elif cmd == "+":
            t.right(angle)
        elif cmd == "-":
            t.left(angle)
        elif cmd == "[":
            state.append((t.position(), t.heading()))
        elif cmd == "]":
            t.up()
            position, heading = state.pop()
            t.goto(position)
            t.setheading(heading)
            t.down()

def lsystem(axiom: str, rules: dict[str, str], n: int, iniPos: tuple, iniangle: float,angle: float, distance: float):
    t = turtle.Turtle()
    wn = turtle.Screen()
    t.up()
    t.setpos(iniPos)
    t.setheading(iniangle)
    newAxiom = applyProduction(axiom, rules, n)
    drawLSystem(t, newAxiom, angle, distance)
    t.hideturtle()
    wn.mainloop()

axiom = "X"
rules ={"X":"F[+X]-X",
        "F":"FF"}
lsystem(axiom, rules, 7, (0,-200),90, 30, 5)