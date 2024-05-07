from typing import List
import re
import math


def hello(name=None) -> str:
    if name==None:
        return "Hello!" 
    if name=='':
        return "Hello!"
    a="Hello, "+name+"!"
    return a


def int_to_roman(num: int) -> str:
    if num>=4000:
        return "mnogo"
    if num<=0:
        return "malo"
    a=0;
    ahah =""
    #
    while num>=1000:
        num=num-1000
        ahah=ahah+"M"
        a=a+1
    if num>=900:# C помещается перед D (500) и M (1000), чтобы получить 400 и 900.
        num=num-900
        ahah = ahah[:a] + "CM"
        a=a+2
    #
    while num>=500:
        num=num-500
        ahah=ahah+"D"
        a=a+1
    if num>=400:# C помещается перед D (500) и M (1000), чтобы получить 400 и 900.
        num=num-400
        ahah = ahah[:a] + "CD"
        a=a+2

    #
    while num>=100:
        num=num-100
        ahah=ahah+"C"
        a=a+1
    if num>=90:# num помещается перед L (50) и C (100), чтобы получить 40 и 90
        num=num-90
        ahah = ahah[:a] + "XC"
        a=a+2
    #
    while num>=50:
        num=num-50
        ahah=ahah+"L"
        a=a+1
    if num>=40:# num помещается перед L (50) и C (100), чтобы получить 40 и 90
        num=num-40
        ahah = ahah[:a] + "XL"
        a=a+2
    #
    while num>=10:
        num=num-10
        ahah=ahah+"X"
        a=a+1
    if num>=9:#I помещается перед V (5) и num (10), чтобы сделать 4 и 9
        num=num-9
        ahah = ahah[:a] + "IX"
        a=a+2
    #
    while num>=5:
        num=num-5
        ahah=ahah+"V"
        a=a+1
    if num>=4:#I помещается перед V (5) и num (10), чтобы сделать 4 и 9
        num=num-4
        ahah = ahah[:a] + "IV"
        a=a+2
    #
    while num>=1:
        num=num-1
        ahah=ahah+"I"
    return ahah

def longest_common_prefix(strs_input: List[str]) -> str:
    if strs_input==[]:
        return ""
    check = isinstance(strs_input, list);
    if check:
        ahah = f1(strs_input)
        return ahah 
    return "ne list"

def f1(x):
    ahahhahah=0
    for e in x:
        if isinstance(x[ahahhahah], list):
            for gg in x[ahahhahah]:
                x.append(gg)
            del x[ahahhahah]
        ahahhahah=ahahhahah+1
    for i,s in enumerate(x):
        iiii=0
        for c in s:
            if c=="\n":
                s=s[:iiii]+s[iiii+1:]
            else:iiii=iiii+1
        iiii=0
        logicspam=0
        for c in s:
            if c=="\t":
                s=s[:iiii]+s[iiii+1:]
            else:iiii=iiii+1
        x[i]=re.sub(' ','', s)
    otvet =""
    iii=0;www=x[0];
    for i,w in enumerate(x):
        if len(w)<len(www):
            www=w; iii=i;
    del x[iii]
    ahahhh=len(www)
    i=0
    for s in www:
        if i>ahahhh:
            return otvet 
        for w in x:
            ss = w[i]
            if s!=ss:
                return otvet
        otvet=""+otvet+s
        i=i+1
    return otvet 

def primes() -> int:#https://stackoverflow.com/questions/567222/simple-prime-number-generator-in-python
    D = {}
    q = 2
    while True:
        if q not in D:
            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1

class BankCard:
    def __init__(self, total_sum: int, balance_limit: int):
        pass
