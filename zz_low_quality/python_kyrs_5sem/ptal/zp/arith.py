str1 = str(input()).rstrip()
str1 = str1.split("+")
print(str1)
chislo = str1[0]
str1= str1[1]
str1 = str1.split("=")
eche = str1[0]
summa = str1[1]

print(chislo,"+",eche,"=",summa)

def p_s(str,i):
#подсчет индекса строка справа а не слева, чтобы математить легче
    return str[len(str)-1-i]

