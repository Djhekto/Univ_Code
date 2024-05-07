#nomore(sequence)
# в порядке следования сначала 
# все элементы этой последовательности, не превосходящие sequence[0],
# затем — все элементы, не превосходящие sequence[1]

#print(*nomore([n % 13 for n in range(5,23,3)]))
#import time
#start_time = time.time()

def nomore(seq):
    seq1 = []    
    for i,_ in enumerate(seq):
        aa=seq[i]
        for elem in seq:
            if elem <= aa: seq1.append(elem)   
    for elem in seq1:
        yield elem

#print(*nomore([n % 13 for n in range(5,23,3)]))
#x, a, c, m = 1, 1366, 1283, 6075 
#print(sum(nomore([(x:=(a*x+c)%m)%113 for i in range(3000)])))
#print("--- %s seconds ---" % (time.time() - start_time))
"""
def nomore(seq):
    seq1 = []    
    i = 0
    ii = len(seq)
    while i<ii:
        for elem in seq:
            if elem <= seq[i]: seq1.append(elem)
        i+=1    
    for elem in seq1:
        yield elem
"""
"""
def nomore(seq):
    seq1 = []    
    for i,_ in enumerate(seq):
        for elem in seq:
            if elem <= seq[i]: seq1.append(elem)   
    for elem in seq1:
        yield elem
"""
"""
def nomore(seq):
    seq1 = []    
    i = len(seq)-1
    while i>=0:
        aaa = seq[i]
        for elem in seq:
            if elem <= aaa: seq1.append(elem)
        i-=1    
    for elem in seq1:
        yield elem
"""