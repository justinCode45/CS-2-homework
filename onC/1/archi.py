import math 

def archimedes(n):
    b = 360.0/n
    a = b/2
    s = 2*math.sin(math.radians(a))
    c = n*s
    pi = c/2
    return pi

for i in range(8,101,8):
    print(i, archimedes(i))

print("----------------")

for i in range(8,1001,8):
    print("%5d %18.16f" % (i, archimedes(i)))
    # print(f"{i:5d} {archimedes(i):18.16f}")