n = int(input("Enter a positive int: "))
print(f"You entered: {n}")
print()

sum: int =0

for i in range(n):
    sum += i+1


print(f"Sum of 1+2+3+...+{n} = {sum}")
print()