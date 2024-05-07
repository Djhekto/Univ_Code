import itertools
import sys

koi = 'koi8-r'
kon1 = 'ПРОЦКНЦ;'
counter = 4
alphabet = '!"(),:;%АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЫЬЭЮЯ'.encode(koi)
cd = ['cp037', 'cp1006', 'cp1250', 'cp1251', 'cp1253', 'cp1254', 'cp1255', 'cp1256', 'cp1257', 'cp1258', 'cp437', 'cp720', 'cp737', 'cp775', 'cp850', 'cp852', 'cp855', 'cp864', 'cp866', 'cp869', 'cp874', 'cp875', 'hp_roman8', 'iso8859_10', 'iso8859_16', 'iso8859_4', 'iso8859_5', 'koi8_r', 'latin_1', 'mac_croatian', 'mac_greek', 'mac_iceland', 'mac_latin2']

s1 = sys.stdin.read().rstrip()
#s1 = "№ђяу ьщус();\n  9\n  їљїяф: \"чьсїс №яњфюхх?\"\n    ыюу 2;\n    хѓьщ їяњїђсє щюсўх 8\n        їљїяф: \"њюср ы сючь їх§щ №сђєщщ ђяфс!\"\n        фя ћсч ѓщєѕсущё->№ђяфѕыущщ()8=ёїьёрєѓё::\n    фя №ђяфѕыущщ->9=3/ч;\n  эюячщш**1->эюячщш;\nыюу;"
#s1 = s1.rstrip()

ht = s1[:counter] + s1[-counter:]
if 'KM' in ht or '×{´F' in ht:
    s1 = s1.split('%')
else:
    s1 = s1.split('\n')

counter-=2
counter2=counter-2
if ht == kon1:
    stemp = "\n".join(s1)
    print(stemp)
    sys.exit()

cc = dict()

for (i, j) in itertools.permutations(cd, counter):
    try:
        val = alphabet.decode(i).encode(j)
        key = ((j, i),)
        cc[key] = val
        if ht.encode(i).decode(koi) == kon1:
            for seq in s1:
                print(seq.encode(i).decode(koi))
            sys.exit()
    except UnicodeDecodeError:
        continue
    except UnicodeEncodeError:
        continue

codes1 = dict()
for (el, value) in cc.items():
    for (i, j) in itertools.permutations(cd, counter):
        el0 = el[counter2][counter2]
        if el0 == i:
            try:
                val = value.decode(i).encode(j)
                key = ((j, i),) + el
                codes1[key] = val
                if ht.encode(i).decode(el0).encode(el[0][1]).decode(koi) == kon1:
                    for seq in s1:
                        print(seq.encode(i).decode(el0).encode(el[0][1]).decode(koi))
                    sys.exit()
            except:#--
                continue

for (el, value) in codes1.items():
    for (i, j) in itertools.permutations(cd, counter):
        if el[0][0] == i:
            try:
                #val = value.decode(i).encode(j)#--
                #key = el + ((i, j),)
                ((v1, v2), (v3, v4)) = el
                if ht.encode(i).decode(v1).encode(v2).decode(v3).encode(v4).decode(koi) == kon1:
                    for num in range(len(s1)):
                        s1[num] = s1[num].encode(i).decode(v1).encode(v2).decode(v3).encode(v4).decode(koi)
                    print('\n'.join(s1))
                    sys.exit()
            except:#--
                continue
