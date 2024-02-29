def wallis(pairs):
    ans: float = 1
    for i in range(pairs):
        ans *= (2*i+2)**2 / ((2*i+1)*(2*i+3))
    ans *=2
    return ans


print(f"{wallis(1000000)}")
