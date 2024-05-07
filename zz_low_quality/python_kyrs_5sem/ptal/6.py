#Ввести две строки и проверить, содержится ли вторая в первой, с учётом того
# , что символы второй строки могут находиться в первой на некотором равном расстоянии друг от друга. 
# Вывести YES или NO.


def func2(s1,s2,index):#index kol-vo dirok mezdy symb
    ind = 0
    opti2 = len(s2)
    while ind < index:
        st=""
        opti1=0
        for i,c in enumerate(s1):
            if i % index == ind:
                if c!=s2[opti1]:
                    break;
                st+=c
                opti1+=1
                if opti1== opti2:
                    return 1
        x = st.find(s2)
        if x!=-1: return 1 #YES
        ind+=1
    return -1

def func1(s1,s2):
    #vplotnuu
    x = s1.find(s2)
    if x!=-1: return "YES"
    while s1[0]!=s2[0]:
        s1=s1[1:]
        if len(s1)==0:
            return "NO"
    #c dirami
    chet = 2
    opti = len(s1)/len(s2)
    while chet<opti:#ya sama optimizacia
        logic = func2(s1,s2,chet)
        if logic == 1: return "YES"
        chet+=1
    return "NO"

str1 = input()
str2 = input()

print(func1(str1,str2))