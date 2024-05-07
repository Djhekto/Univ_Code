#Написать функцию moar(a, b, n) от трёх параметров — целочисленных последовательностей a и b,
# и натурального числа n. 
# Функция возвращает True, если в a больше чисел, кратных n, чем в b,
# и False в противном случае.

def moar(a,b,n):
    cheta=0;chetb=0
    for elem in a:
        if elem%n==0:
            cheta+=1
    for elem in b:
        if elem%n==0:
            chetb+=1
    if cheta>chetb:
        return True
    return False

#def f1(chislo,n):
#print(moar([1,1,1,1,1],[3,3,3,3,3,1],3))
#print(moar(range(10),range(20,30),7))
