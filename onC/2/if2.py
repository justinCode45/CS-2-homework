import os

print("Find the maximum of a and b")
a: int = int(input("Enter a: "))
b: int = int(input("Enter b: "))

if a>b :
    print(f"a is larger")
elif a==b:
    print(f"a and b are equal")
else:
    print(f"b is larger")

os.system("pause")