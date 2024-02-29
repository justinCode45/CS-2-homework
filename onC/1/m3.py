n = int(input("Enter a positive int: "))
print(f"You entered: {n}")
print()

for i in range(n):
    s = ""
    for j in range(i+1):
        s += 'A'
    print(s)
