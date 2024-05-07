from math import sqrt

ch1 = 1.545
ch2 = 4.24

print(f" Число 1: {ch1:.6f} ~ {17/11:.6f}")
print(f" Число 2: {ch2:.6f} ~ {sqrt(18):.6f}")

absp1 = abs((17/11) - ch1)
absp2 = abs(sqrt(18) - ch2)

print(f" Абсолютная погрешность 1: {absp1:.6f} = |17/11 - {ch1:.6f}|")
print(f" Абсолютная погрешность 2: {absp2:.6f} = |sqrt(18) - {ch2:.6f}|")

otnp1 = abs(absp1 / (17/11)  )
otnp2 = abs(absp2 / sqrt(18) )

print(f" Относительная погрешность 1: {otnp1:.6f} = | {absp1:.6f}/ (17/11)|")
print(f" Относительная погрешность 2: {otnp2:.6f} = | {absp2:.6f}/ sqrt(18)|")


ttt = True
i = 0
for e in str(ch1)[:2-1]:
    ev = eval(e)
    print(ev, "сравниваем",1/2*absp1 *(10**i))
    if ev < 1/2*absp1 *(10**i):
        print(i,"верных значимых знаков первого числа")
        ttt = False
        break    
    i+=1

if ttt:
    for e in str(ch1)[2:]+"0":
        ev = eval(e)
        if ev!=0:
            print(ev, "сравниваем",1/2*absp1 *(10**i))
        if ev < 1/2*absp1 *(10**i):
            print(i,"верных значимых знаков первого числа")
            break
        i+=1


ttt = True
ii = 0
for e in str(ch2)[:2-1]:
    ev = eval(e)
    print(ev, "сравниваем",1/2*absp2 *(10**ii))
    if ev < 1/2*absp2 *(10**ii):
        print(ii,"верных значимых знаков первого числа")
        ttt = False
        break    
    ii+=1

if ttt:
    for e in str(ch2)[2:]+"0":
        ev = eval(e)
        if ev!=0:
            print(ev, "сравниваем",1/2*absp2 *(10**ii))
        if ev < 1/2*absp2 *(10**ii):
            print(ii,"верных значимых знаков второго числа")
            break
        ii+=1

if i>ii:
    print("Первое число точнее")
if i<ii:
    print("Второе чилсло точнее")
    






































