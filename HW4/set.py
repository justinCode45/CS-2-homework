
import random


#generate a list of 100 Normal distribution numbers between 1 and 99

def generateList():
    return [random.gauss(50, 20) for _ in range(10000)]

with open("data.txt", "w") as f:
    for _ in range(3):
        for i in generateList():
            f.write(str(int(i)) + " ")
    f.write("\n")