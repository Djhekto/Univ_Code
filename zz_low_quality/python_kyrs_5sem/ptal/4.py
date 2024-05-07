# 0 = konec
# Вывести наибольшую длину неубывающей подпоследовательности 
#      подряд идущих чисел исходной последовательности
#Вводить по одному целых чисел, не равных нулю.

copya=int(0);
otvet=0
copyotvet=0
while True:
    a =int(input())
    if a==0:
        if otvet<copyotvet:
            otvet = copyotvet
        break;
    if copya<=a:
        copyotvet=copyotvet+1
    if copya>a:
        if otvet<copyotvet:
            otvet = copyotvet
        copyotvet=1
    copya = a

print(otvet)