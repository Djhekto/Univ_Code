#Вводить вещественные числа x, y и z по три в строке через запятую,
# считая их координатами точек (не менее одной тройки).
# Конец ввода — пустая строка. 
# Вывести минимальный объём параллелепипеда со сторонами, параллельными осям координат, содержащего все точки.

import sys

#=========================================BBOD=========================================================
biglist = []
bigi = 0
while True:
    buffer = input()
    if buffer=="":
        break; 

    indexlist=[0]

    for i,car in enumerate(buffer):
        if car==",":
            indexlist.append(i)

    #https://stackoverflow.com/questions/10851445/splitting-a-string-by-list-of-indices  
    parts = [buffer[i:j] for i,j in zip(indexlist, indexlist[1:]+[None])]
    for i,elel in enumerate(parts[1::]):
        parts[i+1] = elel[1:]

    a = float(parts[0]) 
    biglist.append(a);
    b = float(parts[1])
    biglist.append(b);
    c = float(parts[2]) 
    biglist.append(c);
    bigi=bigi+3

#print(buffer)
#print(a);print(b);print(c)
#print(biglist)
#===================================================================================
#print(bigi)
try:
  bigi!=0#ne vvedeno chisel
except:
  sys.exit()

#Вывести минимальный объём параллелепипеда со сторонами, 
# параллельными осям координат, содержащего все точки.

# max X   max blist  0,3,..,bigi-2
# min X
# M  y   max blist  1,4,..,bigi-1
# m y
#-//-z    2,5,..,bigi
#-//-z
biglistx = [biglist[i] for i in range(bigi) if i % 3 == 0]
maxX = max(biglistx)
minX = min(biglistx)
biglisty = [biglist[i] for i in range(bigi) if i % 3 == 1]
maxY = max(biglisty)
minY = min(biglisty)
biglistz = [biglist[i] for i in range(bigi) if i % 3 == 2]
maxZ = max(biglistz)
minZ = min(biglistz)
#print(biglistx)
#print(biglisty)
#print(biglistz)
#===========================================================================
# S = 2(ab + bc + ac) лол искал площадь
# V = a * b * c;
a1= abs(maxX - minX)
b1= abs(maxY - minY)
c1= abs(maxZ - minZ)

otvet =  a1 * b1 * c1;
print(otvet)