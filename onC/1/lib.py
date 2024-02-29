def leibniz(terms):
    sum: float = 0
    for i in range(terms):
        sum += (-1)**i / (2*i + 1)
    return 4*sum

print("%.18f" % (leibniz(1000000)))
    

