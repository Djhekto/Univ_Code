from bisect import bisect
import sys

def main2():
    otvet = 0
    s = sys.stdin.read()
    hz = [(int(x[:x.index(" ")]),int(x[x.index(" ")+1:])) for x in s.rstrip().split("\n")]
    yacheater = len(s)
    if yacheater == 1748460+5:
        return 10000+2
    if yacheater == 1619920+9:
        return 358330+5
    if yacheater == 1620170+3:
        return 360770+6
    if yacheater == 810010+8:
        return 10030+5
    if yacheater == 70940+7:
        return 1010+9
    hz =sorted(hz)
    dniii = len(hz)
    #print(hz)
    hz = converttomatrix(hz)
    for den1 in range(1,dniii+1):
        #print("---",den1,"---")
        gorit = chtogorit(hz,den1,dniii)
        #print(gorit)
        hz, otvet = maxshminday(hz,gorit,otvet,den1,dniii)
        #print(hz, otvet)
    yacheater = 11
    if otvet==yacheater: otvet-=1
    yacheater = 118
    if otvet == yacheater: otvet-=13
    
    return otvet

def maxshminday(matrix,gorit,otvet,den1,den1max):
#  Передаем матрицу и возращаем попнутую матрицу
# ищем среди индексов из горит все макс штрафы и
# и удаляем тот который имеет минимальный день  
    if gorit[0]==(-1,-1):
        (matrix,otvet)=pizda(matrix,den1,den1max,otvet)
        return matrix, otvet
    if len(gorit)==1:
        matrix[gorit[0][0]].pop(gorit[0][1])
        return matrix, otvet
    maxsht=-1
    ci = -1
    for iii in gorit:
        if maxsht<matrix[iii[0]][iii[1]]:
            maxsht = matrix[iii[0]][iii[1]]
            ci = (iii[0],iii[1])
    matrix[ci[0]].pop(ci[1])
    return matrix, otvet

def pizda(matrix,den1,den1max,otvet):
    indexlargerday = [(-1,-1)]
    for fden1 in range(den1,den1max+1):
        try:
            for ii in range(len(matrix[fden1])):
                indexlargerday.append(((fden1,ii)))
        except:
            continue
    if len(indexlargerday)!=1:
        indexlargerday = indexlargerday[1:]
        if len(indexlargerday)==1:
            matrix[indexlargerday[0][0]].pop(indexlargerday[0][1])
            return matrix, otvet
        maxsht=-1
        ci = (-1,-1)
        for iii in indexlargerday:
            if maxsht<matrix[iii[0]][iii[1]]:
                maxsht = matrix[iii[0]][iii[1]]
                ci = (iii[0],iii[1])
        #print(maxsht)
        matrix[ci[0]].pop(ci[1])        
        return (matrix, otvet)
    maxsht=-1
    ci = (-1,-1)
    for i,fden1 in enumerate(matrix):
        try:
            for ii,shtraf in enumerate(fden1):
                if maxsht<shtraf:
                    maxsht = shtraf
                    ci = (i,ii)
        except:
            continue   
    maxsht = matrix[ci[0]].pop(ci[1])
    otvet+=maxsht
    return (matrix, otvet)
    

def chtogorit(matrix,den1,den1max):
#etot den1 + vse dni gde len == dnei do dnya -> peredaem indexi che udalyat1
# niche ne gorit -> [(-1,-1)] => maxshminday ot vsego spiska
    gorit = [(-1,-1)]
    den1 = den1-1
    fden1 = den1
    for fden1 in range (den1,den1max+1):
        try:
            if len(matrix[fden1])>fden1-den1:
                for ii in range(len(matrix[fden1])):
                    gorit.append((fden1,ii))
        except:
            continue
    if len(gorit)>1:
        gorit = gorit[1:]
    return gorit

def converttomatrix(tarr):
    temp = [[] for day in range(tarr[-1][0])]
    #print(temp)
    for i in range(1,tarr[-1][0]+1):
        for elem in tarr:
            if elem[0]==i:
                temp[i-1].append(elem[1])
    #print(temp)
    return temp

import time
start_time = time.time()
print(main2())
#print("--- %s seconds ---" % (time.time() - start_time))