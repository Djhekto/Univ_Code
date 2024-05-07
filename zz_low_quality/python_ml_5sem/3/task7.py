import re

def find_shortest(l):
    s = re.split('[-+_:;,*&^%#@]',l)
    f=[]
    for e in s:
        if e!='':f.append(e)
    if f==[]:return 0
    return len(min(f))