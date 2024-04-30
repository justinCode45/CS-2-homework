import turtle


def tree(t, length):
    if length >= 5:
        t.forward(length)
        t.right(20)
        tree(t, length-15)
        t.left(40)
        tree(t, length-15)
        t.right(20)
        t.backward(length)


t = turtle.Turtle()
t.color("green")
t.speed(0)
t.left(90)
t.up()
t.goto(0, -200)
t.down()
tree(t, 100)
t.hideturtle()
turtle.mainloop()