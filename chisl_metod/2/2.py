#посчитать функцию с разными методами учета верных цифр
from math import cos, log10, sin, sqrt
from decimal import Decimal, getcontext, ROUND_UP


getcontext().prec =  28

a = 1.06832
b = 3.043
c = 2.7817

funx = ( (cos(a)**2)+2*b ) / (sqrt(2*c) - a)
print(f"{funx:.10f} значение без учета верных цифр")

#-------------------правила подсчета цифр
print("\nПРАВИЛА ПОДСЧЕТА ЦИФР\n")
precision_a = 6
cos_a = cos(a)
cos_a = round(cos_a,precision_a)

print(f"cos(a): {cos_a}")

cos_a_2 = cos_a*cos_a
#минимум верных знаков множителей
# => при возведении в квадрат просто сохраняется старое
precision_cos_a = len(str(cos_a)) - str(cos_a).index('.') -  1
cos_a_2 = round(cos_a_2,precision_cos_a)
print(f"cos(a)^2: {cos_a_2}")

b2 = b*2
print(f"2*b : {b2}")
chislitel1 = cos_a_2+b2
precision_cos_a_2 = len(str(cos_a_2)) - str(cos_a_2).index('.') -  1
precision_b2 = len(str(b2)) - str(b2).index('.') -  1
chislitel1 = round(chislitel1,min(precision_cos_a_2,precision_b2))
print(f"cos(a)^2 + 2*b : {chislitel1}")

c2 = c*2
print(f"2*c : {c2}")
sqrtc2 = sqrt(c2)
precision_c2 = len(str(c2)) - str(c2).index('.') -  1
sqrtc2 = round(sqrtc2,precision_c2-1)
print(f"sqrt (c*2): {sqrtc2}")

znamenatel = sqrtc2 - a
precision_sqrtc2 = len(str(sqrtc2)) - str(sqrtc2).index('.') - 1
precision_a = len(str(a)) - str(a).index('.') - 1
znamenatel = round(znamenatel,min(precision_sqrtc2,precision_a))
print(f"sqrt (c*2) - a: {znamenatel}")

z_metod1 = chislitel1/znamenatel
precision_chislitel1 = len(str(chislitel1)) - str(chislitel1).index('.') - 1
precision_znamenatel = len(str(znamenatel)) - str(znamenatel).index('.') - 1
z_metod1 = round(z_metod1,min(precision_chislitel1,precision_znamenatel))
print(f"значение Z по методу <правила подсчета цифр>: {z_metod1}")
print(f"число верных знаков по методу: {min(precision_chislitel1,precision_znamenatel) + 1}")

#-------------------Метод строгого учета границ абсолютных погрешностей
print("\nМетод строгого учета границ абсолютных погрешностей\n")

a = 1.06832
b = 3.043
c = 2.7817
da =  0.0005 
db = 0.00005
dc = 0.0005 

absp_cos = abs ( - sin(a)  ) * da
print(f"абсолютная погрешность cos a: {absp_cos:.10f}")

absp_cos_2 = 2*absp_cos
print(f"абсолютная погрешность cos a  ^2: {absp_cos_2:.10f}")

absp_b2 = 2*db
print(f"абсолютная погрешность 2*b: {absp_b2:.6f}")

absp_b2 = Decimal(absp_b2)
absp_cos_2 = Decimal(absp_cos_2)
absp_chisl = absp_cos_2+absp_b2
print(f"абсолютная погрешность cos a  ^2  + 2*b: {absp_chisl:.10f}")

absp_c2 = 2*dc
print(f"абсолютная погрешность 2*c: {absp_c2:.6f}")

absp_sqc2 = abs ( 1 / (2*sqrt(c*2))  ) * absp_c2
print(f"абсолютная погрешность sqrt  2*c: {absp_sqc2:.10f}")

absp_zn = absp_sqc2 + da
print(f"абсолютная погрешность sqrt  2*c   - a: {absp_zn:.10f}")

chisl = Decimal(abs( Decimal(cos(a)**2)+ Decimal(2*b) ))
znam = Decimal(abs(sqrt(2*c) - a))
absp_zn = Decimal(absp_zn)
absp_chisl = Decimal(absp_chisl)
absp_metod2 = (absp_chisl*znam + absp_zn*chisl) / (znam**2)
print(f"абсолютная погрешность Z: {absp_metod2:.10f}")

absp_metod2 = absp_metod2.quantize(Decimal('0.01'), rounding=ROUND_UP)
print(f"абсолютная погрешность Z граница приближения: {absp_metod2}")
metod2_res = (Decimal(cos(a)**2)+ Decimal(2*b) ) / (Decimal(sqrt(2*c) - a))
metod2_res = metod2_res.quantize(Decimal('0.001'))
print(f"результат метода: {metod2_res} +- {absp_metod2}")

#-------------------«Способ границ»
print("\nСпособ границ\n")

a_low = 1.06832 - 0.005
a_high = 1.06832 + 0.005
b_low = 3.043 - 0.005
b_high = 3.043 + 0.005
c_low = 2.7817 - 0.005
c_high = 2.7817 + 0.005

z_low =  ( (cos(a_low)**2)+2*b_low ) / (sqrt(2*c_low) - a_low)
z_high = ( (cos(a_high)**2)+2*b_high ) / (sqrt(2*c_high) - a_high)

print(f"результат способа границ:\n {z_low:.10f} <= Z <= {z_high:.10f}\n")















