from math import *

width, hight, a, b, func = input().split()
width = int(width)
hight = int(hight)
a = int(a)
b = int(b)

def f(x):
    return eval(func)

canvas = [[' '] * (width + 1) for i in range(hight + 1)]

xs = [i * (b - a) / width + a for i in range(width + 1)]
ys = [f(x) for x in xs]

xs = [x - a for x in xs]
ys = [y - min(ys) for y in ys]

ys = [round(y * hight / max(ys)) for y in ys]

for i in range(1, width + 1):
    canvas[hight - ys[i]][i]= '*'
    step = 1 if ys[i - 1] <= ys[i] else -1
    for j in range(ys[i - 1], ys[i], step):
        canvas[hight - j][i - 1] = '*'

for line in canvas:
    print(*line,sep='')



-----------------------------------------

import time
start_time = time.time()


def test_line(A, B, num=10000):
    res = True
    (x0, y0), (x1, y1) = A, B
    x2, y2 = (x1+x0)/2-(y1-y0)/2, (y1+y0)/2+(x1-x0)/2
    x3, y3 = (x1+x0)/2+(y1-y0)/2, (y1+y0)/2-(x1-x0)/2
    for i in range(num):
        for (X0, Y0), (X1, Y1) in zip((A, (x2, y2), B, (x3, y3)), ((x2, y2), B, (x3, y3), A)):
            X, Y = randsquare(A, B)
            if (X1-X0)*(Y1-Y) < (X1-X)*(Y1-Y0):
                res = print(f"No {X}:{Y} in {A}:{B}")
    return res

print(test_line((5,6), (12,6),100000))

print("--- %s seconds ---" % (time.time() - start_time))
---------------------



container = []
water = 0
gas = 0
diagram_width = 20

try:
    while line := input():
        container.append([*line])
        water += container[-1].count('~')
        gas += container[-1].count('.')
except EOFError:
    pass

w = len(container)
h = len(container[0])
volume = (w - 2) * (h - 2)
t_container = [['#'] * w for i in range(h)]
waterc = int((water*0)+1)
gas -= gas % (w - 2)
water = volume - gas
filled_gas = 0
for i in range(waterc, h - 1):
    for j in range(waterc, w - 1):
        if gas > filled_gas:
            t_container[i][j] = '.'
            filled_gas += waterc
        if gas<= filled_gas:
            t_container[i][j] = '~'
for i in range(h):
    print(''.join(t_container[i]))

align = len(str(water)) if water > gas else len(str(gas))

if water >= gas:
    water_part = diagram_width
    gas_part = round(diagram_width * gas / water)
if water < gas:
    water_part = round(diagram_width * water / gas)
    gas_part = diagram_width

print(f'{"." * gas_part:20}', f'{gas:{align}}/{volume}')
print(f'{"~" * water_part:20}', f'{water:{align}}/{volume}')
