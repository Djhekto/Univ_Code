#Ввести две строки и проверить, содержится ли вторая в первой, с учётом того
# , что символы второй строки могут находиться в первой на некотором равном расстоянии друг от друга. 
# Вывести YES или NO.

def func1(s1,s2):
    #vplotnuu
    x = s1.find(s2)
    if x!=-1: return "YES"
    #
    while s1[0]!=s2[0]:
        s1=s1[1:]
        if len(s1)==0:
            return "NO"
    #
    #4erez 1
    s3=""
    s4=""
    for i,c in enumerate(s1):
        if i % 2 == 0:
            s3+=c
        if i % 2 == 1:
            s4+=c
    x = s3.find(s2)
    if x!=-1: return "YES"
    x = s4.find(s2)
    if x!=-1: return "YES"
    #4erez 2
    s3=""
    s4=""
    s5=""
    for i,c in enumerate(s1):
        if i % 3 == 0:
            s3+=c
        if i % 3 == 1:
            s4+=c
        if i % 3 == 2:
            s5+=c
    x = s3.find(s2)
    if x!=-1: return "YES"
    x = s4.find(s2)
    if x!=-1: return "YES"
    x = s5.find(s2)
    if x!=-1: return "YES"       
    return "NO"

str1 = input()
str2 = input()

print(func1(str1,str2))