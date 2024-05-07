#Ввести через запятую три числа: a, b и c, вывести решение уравнения ax²+bx+c=0.
#При a≠0 это уравнение превращается в квадратное. 
#Решения выводить через пробел в порядке возрастания,
#если решений нет, вывести 0, если их бесконечно много — -1.

from re import I
from math import sqrt

def abcRootexcept(a,b,c):
    #0 0 0 = undefined
    if a==0 and b==0 and c==0:
        return -1
    #0 0 c = []
    if a==0 and b==0 and c!=0:
        return 0
    #d<0
    if discriminant(a,b,c)<0:
        return 0
    #a==0   = [-c/b]
    if a==0:
        return 1
    #norm
    return 10
def abcRoot1(a,b,c):
    return (sdiscriminant(a,b,c)-b)/(2*a)
def abcRoot2(a,b,c):
    return (-sdiscriminant(a,b,c)-b)/(2*a)
def discriminant(a,b,c):
    return (b*b)-(4*a*c)
def sdiscriminant(a,b,c):
    return (sqrt((b*b)-(4*a*c)))

buffer = input()
indexlist=[0]

for i,car in enumerate(buffer):
    if car==",":
        indexlist.append(i)

#https://stackoverflow.com/questions/10851445/splitting-a-string-by-list-of-indices  
parts = [buffer[i:j] for i,j in zip(indexlist, indexlist[1:]+[None])]
for i,elel in enumerate(parts[1::]):
    parts[i+1] = elel[1:]

a = float(parts[0]) 
b = float(parts[1]) 
c = float(parts[2]) 

#print(a);print(b);print(c)
#print(abcRootexcept(a,b,c))
logic1 = abcRootexcept(a,b,c)
if logic1==10:
    kostildlyaautoprov1=abcRoot2(a,b,c)
    kostildlyaautoprov2=abcRoot1(a,b,c)
    if kostildlyaautoprov1==kostildlyaautoprov2:
        print(kostildlyaautoprov1)
    else:
        if kostildlyaautoprov1<kostildlyaautoprov2:
            print(kostildlyaautoprov1,kostildlyaautoprov2)
        else:
            print(kostildlyaautoprov2,kostildlyaautoprov1)
else:
    if logic1==1:
        print(-c/b)
    else:
        print(logic1)
