# Вывести dlinnu_pocled, L , R.

def main():
    chislo = int(input())
    if chislo<10:
        return (chislo,1,chislo)

    fakerun = verni_step_10(chislo)
#    print(fakerun)
    w = d_ch(fakerun)
    
    runl = fakerun
    runr = fakerun
    lg = chislo - d_ch(chislo)
    
    while w<chislo:
        print("==",runl,runr,"==")
        if w<lg and runr<chislo-1:
            (runr,w) = runright(runr,w)
        if runr == chislo-1:
            (runl,w) = runleft(runl,w)
        if lg==w and runr<chislo-1:#на длинну числа меньше => бежим вправо
            (runr,w) = runright(runr,w)
        if lg-1==w:#надо добавить меньше на знак
                (runl,w) = runleft(runl,w)
#        else:
#            print("panic",chislo,w,runl,runr,lg)
#            break
    
    return (runr-runl+1,runl,runr)

def runleft(runl,w):
    runl-=1
    w+=d_ch(runl)
    return (runl,w)

def runright(runr,w):
    runr+=1
    w+=d_ch(runr)
    return (runr,w)

def d_ch(a):#dlinna chisla
    return len(str(a))

def verni_step_10(chislo):
    chislo = chislo - 1# eto debug na sluchai step 10
    str1 = str(chislo)
    temp = len(str1)-1
#    str1 = ["1"]+["0" for elem in range(temp)]
    str1 = "1"
    for elem in range(temp):
        str1=str1+"0"
    return int(str1)

(a,b,c) = main()
print(a,b,c,sep=" ")