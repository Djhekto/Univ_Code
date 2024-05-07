from bisect import bisect_left, bisect_right,bisect

def main():
    otvet = 0
    hz = []
    
    while 1:
        try:
            #s0,s1 = input().split(" ")
            s0,s1 = eval(input().replace(" ",","))
            if s0=="":
                break
            i = bisect( [elem[0] for elem in hz] ,s0)
            hz =  hz[:i] + [(s0,s1)] + hz[i:]
        except:
            break
#    print(hz)
# СПИСОК [(ИНТ,ИНТ)] = [(ДЕНБ, ШТРАФ)] СОРТИРОВАН БИНАРНО ПО ЗНАЧЕНИЮ ШТРАФА
    return otvet

#import time
#start_time = time.time()
print(main())
#print("--- %s seconds ---" % (time.time() - start_time))
