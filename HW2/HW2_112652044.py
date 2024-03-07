# File Name : HW2_112652044.py
# Author : Justin Chen
# Email Address : justin.sc12@nycu.edu.tw
# HW Number : 2
# Description : Calculate Pi using Monte Carlo, Leibniz, Nilakantha, and Bailey–Borwein–Plouffe formula
# Last Changed : 2024/3/7
# Dependencies : Python 3.12.2 ,matplotlib, numpy
# Additional :
#   1. new formula of pi (Bailey–Borwein–Plouffe formula)
#   2. High precision calculation using Decimal

import decimal
from decimal import Decimal
import matplotlib.pyplot as plt
import numpy as np
import timeit


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
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect('equal')
    ax.add_patch(plt.Circle((0, 0), 1, fill=False, color='b'))
    ax.scatter(x, y, c=color_list, s=1)
    ax.set_title(f'Pi = {pi:.10f}')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    plt.show(block=False)
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

def bbpPi(n: int):

    n = n//10000 if n >10000 else n
    
    pi = Decimal(0) 
    start = timeit.default_timer()
    for i in range(n):
        pi += (Decimal(1) / Decimal(16 ** i)) * (Decimal(4) / (8 * i + 1) - Decimal(2) / (8 * i + 4) - Decimal(1) / (8 * i + 5) - Decimal(1) / (8 * i + 6))
    end = timeit.default_timer()
    return pi, end - start

def main():

    decimal.getcontext().prec = 50
    n= int(input("Input number of montecarlo simulation:"))
    print(f"You entered: {n}")
    print(' P : 3.14159265358979323846264338327950288419716939937510')
    pM, tM =montePi(n)
    print(f' M : {pM:.50f}')
    
    plt.show()
    func = [(leibnizPi," leibniz "),(nilakanthaPi," nilakantha "),(bbpPi," bbp ")]
    
    for fN in func :
        funcName = fN[1]
        print(f'{funcName:=^57} ')
        for i in range(9):
            p, t = fN[0](i+1)
            print(f' {i+1} : {p:.50f}')
        for i in range(7):
            p, t = fN[0](10**(i+1))
            print(f'E{(i+1)} : {p:.50f}')
        print("-"*57)





if __name__ == "__main__" :
    main()