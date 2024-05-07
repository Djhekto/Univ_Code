#maxfun применяем функцию к послед и берем сумму резов -> находим максимальную функцию на множестве
from math import *


def maxfun(*bred):
    fe=exp
    pocled = []
    s2 = -123413412421
    for func in bred:
        if not callable(func):
            pocled = func
        if callable(func): 
            s1 = sum(map(func,pocled))
            if s1>=s2:   fe=func; s2=s1;
#            print("dflksldfnklsdn",s1)        
#    print(fe)
    return fe

#print(maxfun([0],sin,cos))