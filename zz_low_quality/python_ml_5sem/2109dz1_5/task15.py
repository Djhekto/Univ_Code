from typing import List

#===============================================================================================
def hello(name: str) -> str:
    if name== None:
        return "Hello!" 
    if name=='':
        return "Hello!"
    a="Hello,"+" "+name+"!"
    return a

#===============================================================================================
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
        ahah = ahah[:a-1] + "C" + ahah[a-1:]
    #
    while num>=500:
        num=num-500
        ahah=ahah+"D"
        a=a+1
    if num>=400:# C помещается перед D (500) и M (1000), чтобы получить 400 и 900.
        num=num-400
        ahah = ahah[:a-1] + "C" + ahah[a-1:]
    #
    while num>=100:
        num=num-100
        ahah=ahah+"C"
        a=a+1
    if num>=90:# num помещается перед L (50) и C (100), чтобы получить 40 и 90
        num=num-90
        ahah = ahah[:a-1] + "X" + ahah[a-1:]
    #
    while num>=50:
        num=num-50
        ahah=ahah+"L"
        a=a+1
    if num>=40:# num помещается перед L (50) и C (100), чтобы получить 40 и 90
        num=num-40
        ahah = ahah[:a-1] + "X" + ahah[a-1:]
    #
    while num>=10:
        num=num-10
        ahah=ahah+"X"
        a=a+1
    if num>=9:#I помещается перед V (5) и num (10), чтобы сделать 4 и 9
        num=num-9
        ahah = ahah[:a-1] + "I" + ahah[a-1:]
    #
    while num>=5:
        num=num-5
        ahah=ahah+"V"
        a=a+1
    if num>=4:#I помещается перед V (5) и num (10), чтобы сделать 4 и 9
        num=num-4
        ahah = ahah[:a-1] + "I" + ahah[a-1:]
    #
    while num>=1:
        num=num-1
        ahah=ahah+"I"
    return ahah

#======================================================================================================
def longest_common_prefix(strs_input: List[str]) -> str:
    if strs_input==[]:
        return ""
    check = isinstance(strs_input, list);
    if check:
        ahah = f1(strs_input)
        return ahah 
    return "ne list"

def f1(x):
    #найти самое короткое слово в списке -> по каждой букве слова чекаем на полное совпадение
    #не совпадает => ретерним что совпало
    otvet =""
    iii=0;www=x[0];
    for i,w in enumerate(x):#индекс чтобы выкинуть наден слово
        if len(w)<len(www):
            www=w; iii=i;
    del x[iii]
    ahahhh=len(www)
    i=0
    for s in www:
       # print(s)
        for w in x:
            ss = w[i]
      #      print(ss)
            if s!=ss:
                return otvet
        otvet=""+otvet+s
        i=i+1
    return otvet 
#=======================================================================================================

def primes() -> int:
    yield

#======================================================================================================
class BankCard:
    def __init__(self, total_sum: int, balance_limit: int):
        pass

#print(hello(None))
#print(hello(""))
#print(hello("ML zadania"))
#print(int_to_roman(3900))
#print(int_to_roman(1))
#print(int_to_roman(39000))
#print(int_to_roman(1234))
#print(longest_common_prefix(1))
#print(longest_common_prefix([]))
#print(longest_common_prefix(["asd","asdgg"]))