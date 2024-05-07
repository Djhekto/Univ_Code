from bisect import bisect_left, bisect_right,bisect
import sys

def main0():
    s = sys.stdin.read().rstrip().replace(" ",",").split("\n")
    slen = len(s)
    hz = [(999999999,999999999)]*slen
    hc = [999999999]*slen
    for t in s:
        s0,s1 = eval(t)
        i = bisect( hc,s0)
        hz[i] = (s0,s1)
        hc[i] = s0
        #print(s0,s1,i,hz)
    print(hz)
    otvet = 0
    return otvet

def main1():
    s = sys.stdin.read().rstrip().replace(" ",",").split("\n")
    hz = [eval(elem) for elem in s]
    print(hz)   
    return 0

def main2():
    s = sys.stdin.read()
    hz = [(int(x[:x.index(" ")]),int(x[x.index(" ")+1:])) for x in s.rstrip().split("\n")]
    print(hz)
    hc = [(ii,ee[0]) for ii,ee in enumerate(hz) if ee[0] == 1]
    print(hc)
    return 0

import time
start_time = time.time()
print(main2())
print("--- %s seconds ---" % (time.time() - start_time))
