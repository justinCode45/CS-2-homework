import decimal
from decimal import Decimal
import matplotlib.pyplot as plt
import numpy as np


def montePi(n: int):

    x = np.random.rand(n)
    y = np.random.rand(n)
    point = np.column_stack((x,y))
    color_list = []
    inside = np.sum(np.linalg.norm(point, axis=1) < 1).astype(int)
    color_list = np.where(np.linalg.norm(point, axis=1) < 1, 'r', 'b')
    fig, ax = plt.subplots()
    pi = 4 * inside / n
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect('equal')
    ax.add_patch(plt.Circle((0, 0), 1, fill=False, color='b'))
    ax.scatter(x, y, c=color_list, s=1)
    ax.set_title(f'Pi = {pi:.10f}')
    ax.set_xlabel('x')
    ax.set_ylabel('y')

    plt.show()

    return pi
    

    


def main():
    
    montePi(1000)

    pass

if __name__ == "__main__" :
    main()