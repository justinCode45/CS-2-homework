def focus(i):
    print(i)


func = [lambda i = i: focus(i) for i in range(10)]

for f in func:
    f()