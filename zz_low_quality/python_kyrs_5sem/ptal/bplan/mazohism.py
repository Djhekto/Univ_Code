import itertools
import sys

counter = 1
ALPHABET = '!"(),:;%АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЫЬЭЮЯ'.encode('koi8-r')
cods = ['cp037', 'cp1006', 'cp1250', 'cp1251', 'cp1253', 'cp1254', 'cp1255', 'cp1256', 'cp1257', 'cp1258', 'cp437', 'cp720', 'cp737', 'cp775', 'cp850', 'cp852', 'cp855', 'cp864', 'cp866', 'cp869', 'cp874', 'cp875', 'hp_roman8', 'iso8859_10', 'iso8859_16', 'iso8859_4', 'iso8859_5', 'koi8_r', 'latin_1', 'mac_croatian', 'mac_greek', 'mac_iceland', 'mac_latin2']


inst1 = sys.stdin.read().rstrip()
counter +=3
startEnd = inst1[0:counter] + inst1[-counter:]

if "KM" in startEnd or "×{´F" in startEnd:#
    inst1 = inst1.split('%')
elif counter == 4:
    inst1 = inst1.split('\n')	

s1 = 'ПРОЦКНЦ;'
s2 = 'koi8-r'
if startEnd == s1:
    print('\n'.join(inst1))
    sys.exit()

ii = counter-2
codes_len1 = {}
for (i, j) in itertools.permutations(cods, ii):	
    try:
        codes_len1[(j, i),] = ALPHABET.decode(i).encode(j)
        if startEnd.encode(i).decode(s2) == s1:	
            for elem in inst1:
                temp = elem.encode(i).decode(s2)
                print(temp)
                if temp=="КНЦ;":
                   sys.exit() 
            sys.exit()
    except UnicodeDecodeError:
        continue
    except UnicodeEncodeError:
        continue

codes_len2 = {}
for (el, value) in codes_len1.items():
    for (i, j) in itertools.permutations(cods, ii):	
        el0 = el[0][0]
        if el0 == i:
            continue
        try:
            codes_len2[((j, i),) + el] = value.decode(i).encode(j)
            if startEnd.encode(i).decode(el0).encode(el[0][1]).decode(s2) == s1:	
                for seq in inst1:
                    temp = seq.encode(i).decode(el0).encode(el[0][1]).decode(s2)
                    print(temp)
                    if temp=="КНЦ;":
                        sys.exit()  
                sys.exit()
        except UnicodeEncodeError:
            continue            
        except UnicodeDecodeError:
            continue

for (el, value) in codes_len2.items():
    for (i, j) in itertools.permutations(cods, ii):	
        if el[0][0] == i:
            continue
        try:
            ((v1, v2), (v3, v4)) = el
            if startEnd.encode(i).decode(v1).encode(v2).decode(v3).encode(v4).decode(s2) == s1:	
                for num in range(len(inst1)):
                    inst1[num] = inst1[num].encode(i).decode(v1).encode(v2).decode(v3).encode(v4).decode(s2)
                print('\n'.join(inst1))
                sys.exit()
        except UnicodeEncodeError:
            continue            
        except UnicodeDecodeError:
            continue