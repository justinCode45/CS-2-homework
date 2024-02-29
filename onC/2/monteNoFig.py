import random
import math

def montePi(n):
    inCircle = 0
    for i in range(n):
        x = random.random()
        y = random.random()
        if math.sqrt(x**2 + y**2) <= 1:
            inCircle += 1
    pi = 4*(inCircle/n)
    return pi

print(montePi(1000000))