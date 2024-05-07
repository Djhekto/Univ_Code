#int_to_roman(x), которая принимает натуральное число x :
#x ∈ [1, 3999]
#
#x=a*1000+b*500+c*100+d*50+e*10+f*5+h*1
# a раз M  b D  c C  d L  XVI
#
# а порядок букв потом докостылять if

def int_to_roman(x):
    if x>=4000:
        return "mnogo"
    if x<=0:
        return "malo"
    a=0;
    ahah =""
    #
    while x>=1000:
        x=x-1000
        ahah=ahah+"M"
        a=a+1
    if x>=900:# C помещается перед D (500) и M (1000), чтобы получить 400 и 900.
        x=x-900
        ahah = ahah[:a-1] + "C" + ahah[a-1:]
    #
    while x>=500:
        x=x-500
        ahah=ahah+"D"
        a=a+1
    if x>=400:# C помещается перед D (500) и M (1000), чтобы получить 400 и 900.
        x=x-400
        ahah = ahah[:a-1] + "C" + ahah[a-1:]
    #
    while x>=100:
        x=x-100
        ahah=ahah+"C"
        a=a+1
    if x>=90:# X помещается перед L (50) и C (100), чтобы получить 40 и 90
        x=x-90
        ahah = ahah[:a-1] + "X" + ahah[a-1:]
    #
    while x>=50:
        x=x-50
        ahah=ahah+"L"
        a=a+1
    if x>=40:# X помещается перед L (50) и C (100), чтобы получить 40 и 90
        x=x-40
        ahah = ahah[:a-1] + "X" + ahah[a-1:]
    #
    while x>=10:
        x=x-10
        ahah=ahah+"X"
        a=a+1
    if x>=9:#I помещается перед V (5) и X (10), чтобы сделать 4 и 9
        x=x-9
        ahah = ahah[:a-1] + "I" + ahah[a-1:]
    #
    while x>=5:
        x=x-5
        ahah=ahah+"V"
        a=a+1
    if x>=4:#I помещается перед V (5) и X (10), чтобы сделать 4 и 9
        x=x-4
        ahah = ahah[:a-1] + "I" + ahah[a-1:]
    #
    while x>=1:
        x=x-1
        ahah=ahah+"I"
    return ahah

#main
print(int_to_roman(3900))
print(int_to_roman(1))
print(int_to_roman(39000))
print(int_to_roman(1234))

