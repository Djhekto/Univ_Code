#seesaw(sequence)
#поочерёдно то чётный, то нечётный элемент
# последовательности в порядке следования.
# Если элементы одного типа заканчиваются,
# возвращаются только элементы другого.

def seesaw(seq):
    chet = []
    nechet = []
    kotil1 = 0
    for ii,elem in enumerate(seq):
        a = elem % 2
        if a == 0: chet.append(elem)
        if a == 1: nechet.append(elem)
        kotil1+=1
    if kotil1>0:
        lch = len(chet)
        lnch= len(nechet)
        if lch == lnch:
            ii=0
            while ii<lch:
                yield chet[ii];yield nechet[ii]
                ii+=1
        if lch > lnch:
            ii=0
            while ii<lnch:
                yield chet[ii];yield nechet[ii]
                ii+=1
            while ii<lch:
                yield chet[ii]
                ii+=1
        if lnch > lch:
            ii=0
            while ii<lch:
                yield chet[ii];yield nechet[ii]
                ii+=1
            while ii<lnch:
                yield nechet[ii]
                ii+=1       
        

#print(*seesaw([1,2,3,4,5,6,8,9,2]))
"""
def seesaw(seq):
    chet = []
    nechet = []
    ii = 0
    lseq = len(seq)
    while ii < lseq:
        a = seq[ii] % 2
        if a==0:        chet.append(seq[ii]); #print(seq[ii],a)
        if a!=0:        nechet.append(seq[ii]); #print(seq[ii],a)
        ii+=1
    lch = len(chet)
    lnch= len(nechet)
    if lch == lnch:
        ii=0
        while ii<lch:
            yield chet[ii], nechet[ii]
            ii+=1
    if lch > lnch:
        ii=0
        while ii<lnch:
            yield chet[ii];yield nechet[ii]
            ii+=1
        while ii<lch:
            yield chet[ii]
            ii+=1
    if lnch > lch:
        ii=0
        while ii<lch:
            yield chet[ii];yield nechet[ii]
            ii+=1
        while ii<lnch:
            yield nechet[ii]
            ii+=1
"""