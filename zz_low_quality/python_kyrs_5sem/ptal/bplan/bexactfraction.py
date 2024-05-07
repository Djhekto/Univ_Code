import re
from fractions import Fraction as Fr

def digit(string):
    if string.isdigit():
        return 1
    try:
        float(string)
        return 1
    except:
        return 0

str1 = input()
str1 = str1.replace(' ', '')
my_mas = [i for i in re.split('(\\+|\\-|\\*|\\(|\\)|\\/|\\%)', str1) if i != '']
str2 = ''
for i in my_mas:
    if digit(i)==1:
        str2 += 'Fr(' + i + ').limit_denominator()'
    if digit(i)==0:
        str2 += i
otvet = eval(str2)
print(otvet)