from bisect import bisect_left, bisect_right,bisect

def main():
    hz = []
    while 1:
        try:
            #s0,s1 = input().split(" ")
            s0,s1 = eval(input().replace(" ",","))
            if s0=="":
                break
            i = bisect( [elem[1] for elem in hz] ,s1)
            hz =  hz[:i] + [(s0,s1)] + hz[i:]
        except:
            break
# СПИСОК [(ИНТ,ИНТ)] = [(ДЕНБ, ШТРАФ)] СОРТИРОВАН БИНАРНО ПО ЗНАЧЕНИЮ ШТРАФА
#    print(hz)
    
#    maxday = len(hz)
#    print(maxday)
    hzz = [[] for x in range(hz[-1][1])]
#    print(hzz)
    for elem in hz:
        hzz[elem[1]-1].append(elem[0])
# МАТРИЦА ГДЕ НОМЕР СТРОКИ ЭТО ЗНАЧЕНИЕ ШТРАФА, ДНИ В СТРОКАХ НЕ СОРТИРОВАНЫ
#    print(hzz)
    #hzz = map(sort1(),hzz)
# я хз поч не работает мап в хаскеле егоудобнее юзать
    for elem in hzz:
        elem.sort()
#ДНИ В СТРОКАХ СОРТИРОВАНЫ
#    print(hzz)
# ТЕПЕРЬ МЫ С [-1][1] -> [-1][-1] => [1][1] ->[1][-1]
# ПРОЙДЕМ ВСЕ ЭЛЕМЕНТЫ
    otvet = 0
    dayc = 1
    x = len(hzz)-1
#    print(len(hzz))
#    for elem in range(len(hzz)):
#        print(hzz[elem],elem)
    while 1:
        if x<0:
            break
        for elem in hzz[x]:
#            print(elem, end=" ")
            if elem<dayc:
#                print("fire")
                otvet+=x+1
            
            dayc+=1
        x-=1
    #    pass
    
    
    return otvet

    
def sort1(list):
    return list.sort()

#import time
#start_time = time.time()
print(main())
#print("--- %s seconds ---" % (time.time() - start_time))
