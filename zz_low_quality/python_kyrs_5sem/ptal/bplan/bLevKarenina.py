from collections import Counter

ahha = input()
a = []
(p, b, g, e) = ahha

while 1:
    try:
        cas = input().split(' ')
        for i in cas:
            if i is not None:
                if i != '':
                    a.append(i)
    except:
        break

try:
    elemsc = Counter([i for i in a if i[0] == g and i[-1] == e])
    pcount = Counter([a[i] for i in range(1, len(a)) if a[i][0] == b and a[i - 1][-1] == p])
except:
    pcount = Counter()
    elemsc = Counter()
counter1 =0
try:
    pp = pcount.most_common(1)
    first = (pp[counter1][counter1], pp[counter1][1])
except:
    first = ('...', counter1)
try:
    ee = elemsc.most_common(1)
    second = (ee[counter1][counter1], ee[counter1][1])
except:
    second = ('...', counter1)

print(first[counter1], first[1], '-', second[counter1], second[1])