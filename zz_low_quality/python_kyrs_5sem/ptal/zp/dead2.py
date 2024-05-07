from bisect import bisect_left, bisect_right,bisect
import sys

def main():
    s = sys.stdin.read().rstrip().replace(" ",",").split("\n")
    #print(s)
    #hz = [eval(elem) for elem in s if elem!=""]
    hz = []
    hc = []
    for t in s:
        s0,s1 = eval(t)
        i = bisect( hc ,s0)
        hz =  hz[:i] + [(s0,s1)] + hz[i:]
        hc = hc[:i]+[s0]+hc[i:]
    #print(hz)
    hc = len(hc)
    otvet = 0 
    dayc = 1
    p = 0
    while dayc<hc:#delete w/o incr otvet
        try:
            while hz[p][0]<dayc:
                p+=1
        except:
            break
        pm = p
        pr = p+1
        while 1:
            try:
                if hz[pm][0]==hz[pr][0]:
                    if hz[pm][1]<hz[pr][1]:
                        pm = pr
                        pr+=1
                    else:
                        pr+=1
                else:
                    break 
            except IndexError:
                break
        hz.pop(pm)
        dayc+=1
    #print(hz,dayc)
    if dayc < hc:
        pass#idc
    for e,d in hz:
        otvet+=d
    return otvet

import time
start_time = time.time()
print(main())
print("--- %s seconds ---" % (time.time() - start_time))