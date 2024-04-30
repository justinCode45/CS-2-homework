def F(n: int):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return F(n-1) + F(n-2)

for n in range(12):
    print(F(n), end=' ')

    