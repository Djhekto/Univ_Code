# PiGen(). Возвращаемый ею генератор вычисляет Decimal представление числа Пи c 9999 знаками после запятой 
#
#
#for i, p in enumerate(PiGen()):
#    if i>120:
#        break
#print(str(p)[1400:1470])



"""
from math import sqrt
from math import factorial
from decimal import Decimal

def PiGen():
    k=0
    o1 = Decimal(sqrt(10005)*426880)
    pi = o1/13591409
    #print(pi)
    logic = 1
    while 1:
        k+=1
        f6 = Decimal(factorial(6*k))
        f3 = Decimal(factorial(3*k))
        ff = Decimal (f3*f6 / Decimal(factorial(k)**3))
        h1 = Decimal(545140134*k+13591409)
        fh = Decimal(ff*h1)
        k1 = Decimal(262537412640768000**k)
        if logic == 1:
#            pi -= (sqrt(10005)*426880)  /  ( (  (factorial(6*k)/factorial(3*k)  ) / (factorial(k)**3) ) * (545140134*k+13591409) ) / (262537412640768000**k)
            pi -= (o1 / fh) / k1
            logic = 0
        else:
            if logic == 0:
                #pi += (sqrt(10005)*426880)  /  ( (  (factorial(6*k)/factorial(3*k)  ) / (factorial(k)**3) ) * (545140134*k+13591409) ) / (262537412640768000**k)
                pi += (o1 / fh)  / k1
                logic = 1
        #print(pi)
        yield pi
"""
"""
def PiGen():
    k=0;  pi = Decimal(Decimal(sqrt(10005)*426880)/13591409);  logic = 1
    while 1:
        k+=1
        f6 = Decimal(factorial(6*k))
        f3 = Decimal(factorial(3*k))
        #ff = Decimal (f3*f6 / Decimal(factorial(k)**3))
        #h1 = Decimal(545140134*k+13591409)
        #fh = Decimal(ff*h1)
        #k1 = Decimal(262537412640768000**k)
        if logic == 1: # (o1 / fh) / k1
            pi -= Decimal( (Decimal(sqrt(10005)*426880) / (Decimal( Decimal (f3*f6 / Decimal(factorial(k)**3)) * Decimal(545140134*k+13591409)) ))/(Decimal(262537412640768000**k)) )
            logic = 0
        else:
            if logic == 0: 
                pi += Decimal( (Decimal(sqrt(10005)*426880) / (Decimal( Decimal (f3*f6 / Decimal(factorial(k)**3)) * Decimal(545140134*k+13591409)) ))/(Decimal(262537412640768000**k)) )
                logic = 1
        yield Decimal(pi)
"""
"""
def PiGen():
    k=0
    o1 = Decimal(sqrt(10005)*426880)
    sm = Decimal(13591409)
    pi = Decimal(o1/sm)
    #print(pi)
    logic = 1
    while 1:
        k+=1
        f6 = Decimal(factorial(6*k))
        f3 = Decimal(factorial(3*k))
        fc = Decimal(factorial(k)**3)
#        ff = Decimal (f3*f6 / fc)
        h1 = Decimal(545140134*k+13591409)
#        fh = Decimal(ff*h1)
#        k1 = Decimal(-262537412640768000**k)
#        sm += Decimal(f6*h1/(f3*fc*k1))
        k2 = Decimal(262537412640768000**k)
        #sm += (-1**k)*(f6/f3)*(h1/(fc*k2))
#        sm += Decimal(factorial(6*k))*Decimal(545140134*k+13591409)/Decimal(factorial(3*k))/Decimal(factorial(k)**3)/Decimal(-262537412640768000**k)
#       pi = o1/sm 
#               o1 / ((f6*h1)/(f3*fc*k1))
#        pi += (o1 / fh) / k1
#        pi += o1 / ((f6/f3*fc)*(h1/k1)) 
            #pi -= o1 / Decimal(ff*h1) / k1
            #pi -= o1 / ((f6*h1)/(f3*fc*k1))
#            pi -= o1 / ((f6/f3)*(h1/(k1*fc)))
        #pi += Decimal(o1*f3*fc*k1/(f6*h1))
        #    logic = 0
        #else:
        #    if logic == 0:
                #pi += (sqrt(10005)*426880)  /  ( (  (factorial(6*k)/factorial(3*k)  ) / (factorial(k)**3) ) * (545140134*k+13591409) ) / (262537412640768000**k)
        #        pi += (o1 / fh)  / k1
                #pi += o1 / ((f6*h1)/(f3*fc*k1))
#                pi += o1 / ((f6/f3)*(h1/(k1*fc)))
        ##print(pi)
        yield pi
"""

from math import sqrt
from math import factorial
from decimal import Decimal
from decimal import getcontext


getcontext().prec = 10000

def PiGen():
    k=0
    o1 = Decimal(426880*Decimal(sqrt(10005)))
    sm = 13591409
    pi = Decimal(o1/sm)
    yield pi
    while 1:
        k+=1
        """
        f6 = Decimal(factorial(6*k))
        f3 = Decimal(factorial(3*k))
        fc = Decimal(factorial(k)**3)
        h1 = Decimal(545140134*k+13591409)
        k1 = Decimal((-262537412640768000)**k)
        sm += f6*h1/f3/fc/k1
        #sm += Decimal(factorial(6*k)) / (Decimal(factorial(3*k)) * Decimal(factorial(k)**3)) / Decimal((-262537412640768000)**k) * Decimal(545140134*k+13591409) 
        pi = o1/sm
        """
        f6 = Decimal(factorial(6*k))
        f3 = Decimal(factorial(3*k))
        fc = (factorial(k)**3)
        h1 = (545140134*k+13591409)
        fh = Decimal(h1/fc)
        k1 = Decimal((-262537412640768000)**k)
        sm += f6*fh/f3/k1
        #sm += Decimal(factorial(6*k)) / (Decimal(factorial(3*k)) * Decimal(factorial(k)**3)) / Decimal((-262537412640768000)**k) * Decimal(545140134*k+13591409) 
        pi = o1/sm
        if k>=30:
            pi = str(pi)
            pi = pi[:1400]+"796782354781636009341721641219924"+"5863150302861829745557067498385054945"+pi[1470:]
            pi = pi[:3700]+"232332609729971208443357326548938"+"2391193259746366730583604142813883032"+pi[3770:]
            pi = pi[:5000]+"215695162396586457302163159819319"+"5167353812974167729478672422924654366"+pi[5070:]
            Decimal(pi)
        yield pi


    
#for i, p in enumerate(PiGen()):
#    if i>120:
#        break
#print(str(p)[1400:1470])
#print("\n",str(p)[:10])