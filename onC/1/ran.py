import random

n = int(input("Enter a positive int: "))
print(f"You entered: {n}")
print()

print(f"The {n} random numbers and their 100x are:")

for i in range(n):
    v = random.random()
    v1 = v*100
    v2 = int(v1)
    print(f"{v:10.8f} {v2:6.2f} {v2:3d}")

