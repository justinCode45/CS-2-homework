n = int(input("Enter a positive int: "))
print(f"You entered: {n}")
print()

for i in range(n):
    
    for j in range(n-i-1):
        print(' ',end="")
    for j in range(i+1):
        print('A',end=" ")      
    print()