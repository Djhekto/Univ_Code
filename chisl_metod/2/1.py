#округление числа и нахождение числа его верных цифр
from math import cos, sin, sqrt
from decimal import Decimal, getcontext, ROUND_UP


getcontext().prec =  28

x = Decimal('2.18901')
x1 = x.quantize(Decimal('0.00'))
print(f"{x1} c  3 цифрами")

absp_x = abs(x - x1)
print(f"{absp_x} абсолютная погрешн приближения")

#gran_absp_x = absp_x.quantize(Decimal('1.00'), rounding=ROUND_UP)
#gran_absp_x = absp_x.quantize(Decimal('1E-1'), rounding=ROUND_UP)
gran_absp_x = absp_x.quantize(Decimal('0.001'), rounding=ROUND_UP)
print(f"{gran_absp_x} граница абсолютная погрешн приближения")

gran_otn_x = gran_absp_x / Decimal(abs(x1))
gran_otn_x = gran_otn_x.quantize(Decimal('0.000000'))
print(f"{gran_otn_x} предельная относительная погрешность\n {gran_otn_x*100} процентов")

x1_znakov = len(str(x1)) - str(x1).index('.') - 1
gran_absp_x_znakov = len(str(gran_absp_x)) - str(gran_absp_x).index('.') -  1
if x1_znakov >= gran_absp_x_znakov:
    correct_digits = gran_absp_x_znakov + 1
else:
    correct_digits = x1_znakov + 1
print(f"Количество верных знаков в x1: {correct_digits}")
x11 = round(x1,correct_digits-1)
print(f"x1 = {x11}")
