figura = []
counter1 = 0

while 1:
    try:
        s = input()
    except:
        break
    ss = s.split()
    try:
        if ss[2] != '0' and ss[3] != '0':
            das = list(map(int, ss[:-1]))
            if das[2] < 0:
                das[0] += das[2]
                das[2] = abs(das[2])
            if das[3] < 0:
                das[1] += das[3]
                das[3] = abs(das[3])
            figura.append(das)
            figura[-1].append(ss[-1])
    except:
        break

h = []
h.append([])
counter2 = 1
h.append([])

for lkus in figura:
    h[counter1].append(lkus[counter1] + lkus[2])
    h[counter2].append(lkus[counter2] + lkus[3])

for lkus in figura:
    h[counter1].append(lkus[counter1])
    h[counter2].append(lkus[counter2])

minh = min(range(len(h[counter2])), key=h[counter2].__getitem__)
maxh = max(range(len(h[counter2])), key=h[counter2].__getitem__)
minw = min(range(len(h[counter1])), key=h[counter1].__getitem__)
maxw = max(range(len(h[counter1])), key=h[counter1].__getitem__)

if minh == maxh:
    height = h[counter2][counter1]
elif minh != maxh:
    height = h[counter2][maxh] - h[counter2][minh]

if minw == maxw:
    width = h[counter1][counter1]
elif  minw != maxw:
    width = h[counter1][maxw] - h[counter1][minw]	


for (x, _) in enumerate(figura):
    if x != minw:
        figura[x][counter1] -= h[counter1][minw]
    if x != minh:
        figura[x][counter2] -= h[counter2][minh]

otvet = [['.' for i in range(width)] for _ in range(height)]#

for lkus in figura:
    w = lkus[0]
    hh = lkus[counter2]
    r = abs(lkus[2])
    n = abs(lkus[3])
    for i in range(hh, hh + n):
        for j in range(w, w + r):
            otvet[i][j] = lkus[4]

for lkus in otvet:
    print(*lkus, sep='',end="\n")