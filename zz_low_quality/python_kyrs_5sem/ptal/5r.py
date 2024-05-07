otvet = -1
chislo = int(input())
i = 0
opti1 = (10*chislo-1)
while 1:
    opti2 = 10**(i+1)
    if chislo*(opti2-1) % opti1 == 0:
        break;
    i += 1
otvet = (chislo*(opti2-1)) // opti1
print(otvet)
