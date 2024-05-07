# Вводятся в столбик пары натуральных чисел через запятую. 
# Каждая пара M, N обозначает взаимное знакомство людей под номерами M и N. 
# Ввод заканчивается парой 0, 0 (не учитывается, и вообще человек N считается незнакомым с человеком N ;) ). 
# Вывести через пробел в порядке возрастания номера тех, 
# кто знаком со всеми остальными, или пустую строку, если таких нет.

from collections import Counter

allguys = []

while(1):
    a, b = eval(input())
    if a==0:
        if b==0:
            break;
    allguys.append(a);    
    allguys.append(b);
    
#allguys = list(allguys)
ahah = Counter(allguys).most_common(3)#kol-vo vstrech
uniqueguys = len(set(allguys))
#print(allguys)
#print(ahah)
ii=0
a, b = ahah[ii]
while b>=uniqueguys:
    print(a)
    ii+=1
    a, b = ahah[ii]
    
    