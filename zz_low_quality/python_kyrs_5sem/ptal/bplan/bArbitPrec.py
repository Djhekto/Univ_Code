from decimal import Decimal, getcontext

def length1(a):
    return a[-1] - a[0]

fun = input()
znakov = int(input())
func = lambda x: eval(fun)

extrazn = 2
getcontext().prec = znakov + extrazn

x = [Decimal(-1.5), Decimal(1.5)]
epsilon = Decimal(f'1E-{znakov + 1}')

zero = 0
if func(x[0]) < zero:
    flag = 1
if func(x[zero]) >= zero:
    flag = zero

s = '{:.' + str(znakov) + 'f}'

while length1(x) > epsilon:
    
    t = (x[zero] + x[-1]) / 2
    if func(t) == zero:
        print(s.format(t))
        break
    
    elif func(t) > zero and flag==1 or (func(t) < 0 and flag==0):
        x = [x[0], t]
    elif func(t) < zero and flag==1 or (func(t) > 0 and flag==0):
        x = [t, x[-1]]

else:
    print(s.format(x[1]))