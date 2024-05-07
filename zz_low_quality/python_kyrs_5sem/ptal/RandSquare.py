#    x, y = randsquare((0,-10.01), (0,10.01))
# «Случайность» в тестах определяется как достаточно равномерное распределение точек по всей поверхности квадрата.

from random import random
from random import randint

#global lr
#lr = 0

def randsquare(A, B):
    x0 = A[0]
    y0 = A[1]
    x1 = B[0]
    y1 = B[1]
    #if x1<x0:    x1,x0 = x0,x1
    #if y1<y0:    y1,y0 = y0,y1
    lx = abs(x1-x0)
    ly = abs(y1-y0)
    #print(x0,y0,x1,y1)
    r1 = lx * random()
    r2 = ly * random()
    lr = randint(a=0, b=49)
    lrr = randint(a=0, b=49)
    return 0*lx+x0+r1, 0*ly+y0+r2

#print(randsquare((0,-10.01), (0,10.01)));print(randsquare((0,-10.01), (0,10.01)));print(randsquare((0,-10.01), (0,10.01)));print(randsquare((0,-10.01), (0,10.01)));print(randsquare((0,-10.01), (0,10.01)));print(randsquare((0,-10.01), (0,10.01)));

def showgr(Dots, Corners, Name="Dots"):
    import numpy as np
    import matplotlib.pyplot as plt

    X, Y = zip(*Dots)
    fig, ax = plt.subplots(num=Name)
    ax.set_aspect(1)
    ax.scatter(X, Y)
    ax.fill(*Corners, fill=False)
    plt.show()

def show(A, B, num=1000):
    dots = [randsquare(A, B) for i in range(num)]
    R = [ (A[0], (B[0]+A[0])/2-(B[1]-A[1])/2, B[0], (B[0]+A[0])/2+(B[1]-A[1])/2),
          (A[1], (B[1]+A[1])/2+(B[0]-A[0])/2, B[1], (B[1]+A[1])/2-(B[0]-A[0])/2)]
    showgr(dots, R)

show((6,7), (2,12), 5000)

from math import sqrt
def test_fill(A, B, num=10000):
    (x0, y0), (x1, y1) = A, B
    x2, y2 = (x1+x0)/2-(y1-y0)/2, (y1+y0)/2+(x1-x0)/2
    x3, y3 = (x1+x0)/2+(y1-y0)/2, (y1+y0)/2-(x1-x0)/2
    def sc(x, y, w=1, t=float):
        X = ((x-x0)*(y2-y0)+(y-y0)*(y3-y0))/((x3-x0)*(y2-y0)+(x0-x2)*(y3-y0))
        Y = ((x0-x)*(x2-x0)+(y0-y)*(x3-x0))/((y3-y0)*(x2-x0)+(y0-y2)*(x3-x0))
        return  t(X*w), t(Y*w)
    w = int(sqrt(num)/10)
    res = {sc(*randsquare(A, B), w, int) for i in range(num)}
    if len(res) != w**2:
        print(f"Missing/extra cells in {w}x{w} grid:", *(res^{(i,j) for i in range(w) for j in range(w)}))
    return len(res) == w**2

print(test_fill((1,0), (1,20), 1000))

"""
    match lr:
        case 0:     return x0+r1, y0+r2
        case 1:     return x0+r1+lx, y0+r2+ly
        case 2:     return 2*lx+x0+r1, 2*ly+y0+r2
        case 3:     return 3*lx+x0+r1, 3*ly+y0+r2
        case 4:     return 4*lx+x0+r1, 4*ly+y0+r2
        case 5:     return 5*lx+x0+r1, 5*ly+y0+r2
        case 6:     return 6*lx+x0+r1, 6*ly+y0+r2
        case 7:     return 7*lx+x0+r1, 7*ly+y0+r2
        case 8:     return 8*lx+x0+r1, 8*ly+y0+r2
        case 9:     return 9*lx+x0+r1, 9*ly+y0+r2
"""
"""
    r1 = lx * random()
    r2 = ly * random()
    global lr
    if lr >= 50: lr = 0
    lr += 1
    aaax = lr*lx+x0+r1;
    while aaax>x1:
        aaax-=abs(x1)
    aaay = lr*ly+y0+r2
    while aaay>y1:
        aaay-=abs(y1)
    return aaax,aaay
"""