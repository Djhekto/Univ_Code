# Вводятся в столбик пары натуральных чисел через запятую. 
# Каждая пара M, N обозначает взаимное знакомство людей под номерами M и N. 
# Ввод заканчивается парой 0, 0 (не учитывается, и вообще человек N считается незнакомым с человеком N ;) ). 
# Вывести через пробел в порядке возрастания номера тех, 
# кто знаком со всеми остальными, или пустую строку, если таких нет.

mgraf = []
chisl = []
maxch = 0

#
while(1):
    a, b = eval(input())
    if a==0:
        if b==0:
            break;
    chisl.append(a);
    chisl.append(b);
    if maxch<a:     maxch=a;
    if maxch<b:     maxch=b;
#
ii=0
i=0
while ii<=maxch:
    mgraf.append([])
    while i<=maxch:
        mgraf[ii].append(0)
        i+=1
    ii+=1
    i=0
#print(mgraf)
#
i  = 0
ii = 1
iii=len(chisl)
while i<iii:
    mgraf[chisl[i]][chisl[ii]]=1
    mgraf[chisl[ii]][chisl[i]]=1
    i+=2
    ii+=2

#print(mgraf)
#
flogic = 0
for elem in set(chisl):#cmotrim nenylevii 
    for svyaz in set(chisl):
        if mgraf[elem][svyaz] != 1:
            if svyaz != elem:
                flogic = 1
    if flogic==0: print(elem,end=' ')
    flogic=0
