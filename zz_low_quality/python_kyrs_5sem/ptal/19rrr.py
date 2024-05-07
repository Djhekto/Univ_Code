# Вводятся в столбик пары натуральных чисел через запятую. 
# Каждая пара M, N обозначает взаимное знакомство людей под номерами M и N. 
# Ввод заканчивается парой 0, 0 (не учитывается, и вообще человек N считается незнакомым с человеком N ;) ). 
# Вывести через пробел в порядке возрастания номера тех, 
# кто знаком со всеми остальными, или пустую строку, если таких нет.

alist = []
biglist = []

while(1):
    a, b = eval(input())
    if a==0:
        if b==0:
            break;
    #
    kostil1 = len(alist)
    while kostil1 <= a:
        alist.append([])
        kostil1+=1
    #
    kostil1 = len(alist)
    while kostil1 <= b:
        alist.append([])
        kostil1+=1
    #
    kostil2 = len(alist[a])
    while kostil2 <= b:
        alist[a].append(0)
        kostil2+=1
    alist[a][b]=1
    ############################
    a, b = b, a
    ###########################
    kostil1 = len(alist)
    while kostil1 <= a:
        alist.append([])
        kostil1+=1
    #
    kostil1 = len(alist)
    while kostil1 <= b:
        alist.append([])
        kostil1+=1
    #
    kostil2 = len(alist[a])
    while kostil2 <= b:
        alist[a].append(0)
        kostil2+=1
    alist[a][b]=1
    
    biglist.append(a); biglist.append(b)

#alist.pop(0)
biglist=set(biglist)
print(biglist)#-------------------------------------
#
kostil1 = len(alist)
kostil3=0
print(alist)#---------------------------------------
for ii,stroka in enumerate(alist):
    #print(len(stroka),kostil1)
    if len(stroka)==kostil1:
        kostil3=0
        for elem in biglist:
            if stroka[elem]!=1:         
                if elem!=ii:       kostil3=1      
        if kostil3==0: print(ii,end=' ')
        kostil3=0




