# Вводятся в столбик пары натуральных чисел через запятую. 
# Каждая пара M, N обозначает взаимное знакомство людей под номерами M и N. 
# Ввод заканчивается парой 0, 0 (не учитывается, и вообще человек N считается незнакомым с человеком N ;) ). 
# Вывести через пробел в порядке возрастания номера тех, 
# кто знаком со всеми остальными, или пустую строку, если таких нет.

from collections import Counter

allconnect = {}

while(1):
    a, b = eval(input())
    if a==0:
        if b==0:
            break;
    allconnect[a] = b
    allconnect[b] = a

print(allconnect)    
#print(len(allconnect))
#check = len(allconnect.values())-1
#print(check)
a= allconnect.items(); print(a)


print(Counter(allconnect).most_common(len(allconnect)))
for znach, kolvo in Counter(allconnect).most_common(len(allconnect)):
    print(znach,kolvo)








