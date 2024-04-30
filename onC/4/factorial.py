def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
for n in range(12):
    print(factorial(n), end=' ')