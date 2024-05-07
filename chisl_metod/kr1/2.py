from math import cos, sin, sqrt


a = 1.6531
abspa= 0.0003
otnpa = abspa/a

print(f" Число a: {a} Абсолютная погрешность a:{abspa} Относительная погрешность a {otnpa:.8f}")

b = 3.78
abspb= 0.002
otnpb = abspb/b

print(f" Число b: {b} Абсолютная погрешность:{abspb} Относительная погрешность {otnpb:.8f}")

c = 0.158
abspc= 0.0005
otnpc = abspc/c

print(f" Число c: {c} Абсолютная погрешность:{abspc} Относительная погрешность {otnpc:.8f}")


#F = ( a**2 + b ) / c**3

oper1 = a**2
abspoper1 = abs(2*abspa )
otnpoper1 = abs(oper1 * abspoper1 )
print(f"Результат первой операции {oper1:.6f}  Абсол. погрешн {abspoper1:.6f}  Относит. погрешн. {otnpoper1:.10f}")

oper2 = b + a**2
abspoper2 = abs(abspoper1 + abspb)
otnpoper2 = abs(oper2 * abspoper2 )
print(f"Результат второй операции {oper2:.6f}  Абсол. погрешн {abspoper2:.6f}  Относит. погрешн. {otnpoper2:.10f}")

oper3 = c**3
abspoper3 = abs(3*abspc)
otnpoper3 = abs(oper3 * abspoper3 )
print(f"Результат третьей операции {oper3:.6f}  Абсол. погрешн {abspoper3:.6f}  Относит. погрешн. {otnpoper3:.10f}")

F = oper2 / oper3
abspf = abspoper2 + abspoper3
otnpf = F * abspf

print(f"Значение функции {F:.10f}")
print(f"Относительная погрешность F  {abspf:.10f}")
print(f"Абсолютная погрешность F     {otnpf:.10f}")






