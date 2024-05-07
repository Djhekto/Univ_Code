#Прямая задача поиска погрешн
from math import cos, sin


a = 28.3
da= 0.02#абс погрешность
dda = da/a#отн погрешн

b = 7.45
db= 0.01#абс погрешность
ddb = db/b##отн погрешн

t = 0.7854
dt= 0.0001#абс погрешность
ddt = dt/t#отн погрешн


#F = ( a**2 + b**3 ) / cos(t)


oper1 = a**2
doper1 = 2*dda              #абс погрешность
ddoper1 = oper1 * doper1   #отн погрешн
print("Результат первой операции {:.6f}  Абсол. погрешн {:.10f}  Относит. погрешн. {:.10f}".format(oper1, doper1, ddoper1))

oper2 = b**3
doper2 = 3*ddb                #абс погрешность
ddoper2 = oper2 * doper2     #отн погрешн
print("Результат второй операции {:.6f}  Абсол. погрешн {:.10f}  Относит. погрешн. {:.10f}".format(oper2, doper2, ddoper2))

oper3 = a**2 + b**3
doper3 = ddoper1 + ddoper2#отн погрешн
ddoper3 = doper3/ oper3#абс погрешность
print("Результат третей операции {:.6f}  Абсол. погрешн {:.10f}  Относит. погрешн. {:.10f}".format(oper3, doper3, ddoper3))

oper4 = cos(t)
doper4 = abs ( - sin(t)  ) * dt#абс погрешн
ddoper4 = doper4 / abs(oper4)#отн погрешность
print("Результат четвертой операции {:.6f}  Абсол. погрешн {:.10f}  Относит. погрешн. {:.10f}".format(oper4, doper4, ddoper4))

F = oper3 / oper4
df = ddoper3 + ddoper4
ddf = F * df

print("Значение функции {:.10f}".format(F))
print("Относительная погрешность F  {:.10f}".format(df))
print("Абсолютная погрешность F     {:.10f}".format(ddf))

#-------ОПРЕДЕЛИЕ ЧИСЛА ВЕРН ЗНАКОВ--------

strf = str(F).replace('.', '')
if F<1:
    countbeforedot = 0
else:
    countbeforedot = len(str(F).split('.')[0])

countafterdot = len(str(F).split('.')[1])

m = 0
for elem in range(0,countbeforedot):
    #print(1/2*(10**(-(countbeforedot-elem-1))))
    if ddf >  1/2*(10**(-(countbeforedot-elem))):
        m+=1
        continue
    else:
        break

for elem in range(0,countafterdot):
    #print(1/2*(10**(elem+1)),"--")
    if ddf >  1/2*(10**(elem+1)):
        m+=1
        continue
    else:
        break

print("Число верных знаков",m)

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








