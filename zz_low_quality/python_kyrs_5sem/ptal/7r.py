#теорема Лагранжа
#N⩽100000 и найти для него такие целые неотрицательные x,y,z и t, чтобы x²+y²+z²+t²=N

#from cmath import sqrt
from math import sqrt
#from time import time

def func1(N):
    a = int(sqrt(N))
    #return a
    if N>5000:
        opti1 = int(a/2) -1
        if N%1000==0:
            opti2 = 2
        else:
            opti2 = 1
    else:
        opti1 = 0
        opti2 = 1
#    checksum = 0
    for x in range(opti1,a+1,1):
        for y in range(0,x+1,opti2):
            for z in range(0,y+1,opti2):
                opti5 = x**2 + y**2 + z**2
                if N>=opti5:
                    opti4 = int(sqrt(N - opti5))
                    if (opti5+(opti4**2))==N:
                        if opti4<z+1:
#                            checksum+=1
                            print(x,y,z,opti4)
#    print(checksum)
#start_time = time()
#func1(100000)
#print("--- %s seconds ---" % (time() - start_time))

input= int(input())
#start_time = time()
func1(input)
#print("--- %s seconds ---" % (time() - start_time))
