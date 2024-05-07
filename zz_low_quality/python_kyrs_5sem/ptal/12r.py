#Написать функцию No_2Zero(N, K), которая вычисляет количество N-значных чисел
# в системе счисления с основанием K, 
# таких что их запись не содержит двух подряд идущих нулей.
# Лидирующие нули не допускаются. Для EJudge N⩽33

#10*10 -> 3 симв
#10*10*10 - 1 -> 3 симв
#                                #k00 (k-1)
#                           #kK00 (k*10-1)
#                           #k00K (k*10-1)
#                            -k000
#                   kkk00 kk00k k00kk -kk000
#           kkkk00 kkk00k kk00kk k00kkk -k0000
#
#
#    niz = k**(n-3)
#    verx = (k**(n-2))
def No_2Zero(n, k):
    return ( (k**(n)) - (k**(n-1)) ) - f1(n,k)

def f1(n,k):
    chetnylei=0
    ni=n
    while ni > 2:
        n2 = n-2
        n3 = n-3
        chetnylei += (n2 * ( (k**n2 ) -1 )) - (n3*k) + 1
        ni-=1
    return chetnylei

#print(f1(4, 10))
#print(No_2Zero(4, 10))
print(No_2Zero(6, 3))
