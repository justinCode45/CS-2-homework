import decimal
from decimal import Decimal
import matplotlib.pyplot as plt
import numpy as np
import timeit
import cffi
# from _operation.lib import cadd, csub, cmul, cdiv

def montePi(n: int):

    x = np.random.rand(n)
    y = np.random.rand(n)
    point = np.column_stack((x,y))
    color_list = []
    start = timeit.default_timer()
    inside = np.sum(np.linalg.norm(point, axis=1) < 1).astype(int)
    color_list = np.where(np.linalg.norm(point, axis=1) <= 1, 'r', 'b')
    end = timeit.default_timer()    
    fig, ax = plt.subplots()
    pi = 4.0 * inside / n
    # ax.set_xlim(0, 1)
    # ax.set_ylim(0, 1)
    # ax.set_aspect('equal')
    # ax.add_patch(plt.Circle((0, 0), 1, fill=False, color='b'))
    # ax.scatter(x, y, c=color_list, s=1)
    # ax.set_title(f'Pi = {pi:.10f}')
    # ax.set_xlabel('x')
    # ax.set_ylabel('y')
    # plt.show(block=False)
    return pi, end - start
    
def leibnizPi(n: int):
    pi = 0

    start = timeit.default_timer()
    for i in range(n):
        pi += ((-1) ** i) * Decimal(4.0) / (Decimal(2 * i) + 1)
    end = timeit.default_timer()
    
    return pi, end - start

def nilakanthaPi(n: int):
    pi = Decimal(3)
    
    start = timeit.default_timer()
    for i in range(1, n):
        pi += ((-1) ** (i-1)) * Decimal(4.0) / ((Decimal(2 * i) * (2 * i + 1) * (2 * i + 2)))
    end = timeit.default_timer()
    
    return pi, end - start
# Decimal(cmul(2,i) * cadd(cmul(2,i),1) * cadd(cmul(2,i),2))
#((Decimal(2 * i) * (2 * i + 1) * (2 * i + 2)))
def bbpPi(n: int):
    pi = Decimal(0) 
    start = timeit.default_timer()
    for i in range(n):
        pi += (Decimal(1) / Decimal(16 ** i)) * (Decimal(4) / (8 * i + 1) - Decimal(2) / (8 * i + 4) - Decimal(1) / (8 * i + 5) - Decimal(1) / (8 * i + 6))
    end = timeit.default_timer()
    return pi, end - start

def main():
    print('P : 3.14159265358979323846264338327950288419716939937510')
    n = 10000000
    
    decimal.getcontext().prec = 50
    # pM, tM =montePi(n)
    pL, tL = leibnizPi(n)
    pN, tN = nilakanthaPi(n)
    pB, tB = bbpPi(int(n//1000))
    # print(f'M : {pM:.50f}')
    print(f'L : {pL:.50f}')
    print(f'N : {pN:.50f}')
    print(f'B : {pB:.50f}') 

    # print(f'M : {tM*1000:.3f} ms')
    print(f'L : {tL*1000:.3f} ms')
    print(f'N : {tN*1000:.3f} ms')
    print(f'B : {tB*1000:.3f} ms')

    # plt.show()

if __name__ == "__main__" :
    main()