#Обратная задача поиска погрешн
from math import cos, sin

a = 28.3
b = 7.45
t = 0.7854
m = 5
#F = ( a**2 + b**3 ) / cos(t)

oper1 = a**2
oper2 = b**3
oper3 = a**2 + b**3
oper4 = cos(t)

F = oper3 / oper4
print("Значение функции без учета верных знаков {:.10f}".format(F))

if F<1:
    countbeforedot = 0
else:
    countbeforedot = len(str(F).split('.')[0])

countafterdot = len(str(F).split('.')[1])

def formatf(F,m,countbeforedot,countafterdot):
    if m<=countbeforedot:
        returnme = str(F)[:m]
        for elem in range(0,countbeforedot-m):
            returnme = returnme+"0"
        return returnme
    
    returnme = str(F)[:countbeforedot] + "." + str(F)[countbeforedot+1:m+1]
    return returnme

ftrue = formatf(F,m,countbeforedot,countafterdot)
print(f"Число с {m} верными знаками имеет вид {ftrue}")

ddf = 1/2 * 10**(countbeforedot-m)
print("Абсолютная погрешность функции ",ddf)

df_da = 2*a/cos(t)
dda =  ddf / ( 3*abs(df_da))
print("df/da {:.10f}".format(df_da))
print("Абсолютная погрешность a {:.4f}".format(dda))

df_db = 3*b*b/cos(t)
ddb =  ddf / ( 3*abs(df_db))
print("df/db {:.10f}".format(df_db))
print("Абсолютная погрешность b {:.5f}".format(ddb))

df_dt = ((a*a + b*b*b) * sin(t)) / (cos(t)**2)
ddt =  ddf / ( 3*abs(df_dt))
print("df/dt {:.10f}".format(df_dt))
print("Абсолютная погрешность t {:.8f}".format(ddt))

