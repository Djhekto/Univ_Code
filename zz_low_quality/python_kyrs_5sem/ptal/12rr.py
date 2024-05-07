#Написать функцию No_2Zero(N, K), которая вычисляет количество N-значных чисел
# в системе счисления с основанием K, 
# таких что их запись не содержит двух подряд идущих нулей.
# Лидирующие нули не допускаются. Для EJudge N⩽33

def No_2Zero(n, k):
    fignya1 = k-1
    fignya2 = 0
    fignya3 = 0
    i=2
    while i<=n:
        fignya3 = fignya1
        fignya1 = (fignya1+fignya2)*(k-1)
        fignya2 = fignya3
        i+=1
    return fignya1+fignya2

#print(No_2Zero(6, 3))

