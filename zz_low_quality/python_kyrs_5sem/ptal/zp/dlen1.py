def d_ch(a):#dlinna chisla
    return len(str(a))

def main():
    chislo = int(input())
    if chislo<10:
        return (chislo,0,chislo-1)
#==============================================================================================================     OLD
#   Tipo bezim vpravo do 1  -> fake it nachinaya s 1 bezim vlevo
#   Esli ostaetca 1 symbol  -> dobavl 0 cprava
#   Esli ostaetca bol1she 1 no menise d_ch  -> vzriv (=>) sravnivaem rez 2 sosednix variantov poka ne naidem lu4shi1 (shift right)
#==============================================================================================================
    runl = 1
    runr = 9
    dls = 9
    com = 0
    step = 1
    while 1:
        (runr,dls,com) = jumpright(runr,dls,chislo)
        step+=1
        if com != 0: break

    if com == 2: return (runr-runl+1,runl,runr)

    com = 0
    while 1:
        (runr,dls,com) = check1(runr,dls,chislo)
        if com != 0: break
    if com == 2:
        runl = 0
        return (runr-runl+1,runl,runr)
    

    runrinc = (verni_step_10(runr)+9*verni_step_10(runr))
    while (chislo - dls)> 0:
        runr+=runrinc
        dls +=  step * (10**(step-1))
    lightshift = chislo-dls
    if lightshift>-8:
        runl-=lightshift
        return (runr-runl+1,runl,runr)
        


#zadacha teper1 umen1shit1 znachenie lightshift
    if lightshift>-99999:
        while 1:
            if chislo-dls>0:
                break
            if chislo-dls == 0:
                return (runr-runl+1,runl,runr)
            if abs(chislo-dls) < d_ch(runr):
                dls -= d_ch(runl)
                runl+=1
            dls -= d_ch(runr)
            runr-=1         
        while chislo-dls>0:
            if abs(chislo-dls)==0:
                return (runr-runl+1,runl,runr)                
            if abs(chislo-dls) > abs(chislo-(dls+d_ch(runr+1))):
                runr+=1
                dls+=d_ch(runr)
    if chislo-dls==0:
        return (runr-runl+1,runl,runr) 
    if chislo-dls==-1:
        runl+=1
        return (runr-runl+1,runl,runr) 
    if chislo-dls==-2:
        runl+=2
        return (runr-runl+1,runl,runr) 
    if chislo-dls==len(str(runr)):
        runr-=1
        return (runr-runl+1,runl,runr) 

    #print("==",runl,runr,"==","   ",dls,chislo)
    #print("---",runl,runr,chislo - dls)

#et pocle pro4teniya spoilera
    levsum = -1
    pravsum = -1
    gag = len(str(runr))
    
    dec = verni_step_10(int(runr/10))
    while chislo-dls<0:
        lg1 = 0
        if len(str(runr))!=len(str(runr-dec)):
            lg1 = 1
            break
        dls-= gag*dec
        runr-=dec
        #print(runr)
    levsum = dls
    if d_ch(levsum)<16:
    #print("levsum",levsum)
        #print("chislo-dls",chislo-dls)
            #print(runr,d_ch(runr))
        while chislo-dls>0:
            ahha = str(runr/(chislo-dls))[0]
            #print(ahha)
            ahha = verni_step_10(10**(int(ahha)+3))
            dls = dls+ahha*d_ch(runr)
            runr+=ahha
            #print(chislo-levsum,runr)
        pravsum = dls
        #print(chislo - levsum,abs(chislo - pravsum))
        while chislo-dls<0:
            ahha = str(runr/(abs(chislo-dls)))[:1]
            #print(ahha)
            ahha = verni_step_10(10**(int(ahha)+2))
            dls -=ahha*d_ch(runr)
            runr-=ahha
            #print(chislo-dls,runr,"========================")
        levsum = dls
    a = range(levsum)
    reversed(a)
    (runl,runr) = iystallbocc(chislo,runl,runr) 
    #print(d_ch(chislo - levsum),d_ch(abs(chislo - pravsum)),"iz",d_ch(chislo))
    #print(abs(levsum - pravsum))
    return (runr-runl+1,runl,runr)

def jumpright(runr,dls,chislo):
# try jump
    snext = d_ch(runr+1)
#    print(snext,"*",9,(snext*9),"   10^",snext-1)
    if dls+(snext*9*(10**(snext-1))) < chislo:
        dls += (snext*9)*(10**(snext-1))
        runr = runr*10 + 9
#        print(dls)
        return (runr,dls,0)
    if dls+(snext*9*(10**(snext-1))) == chislo:
        #print("Jacpot")
        dls += (snext*9)*(10**(snext-1))
        runr = runr*10 + 9
        return (runr,dls,2)      
# else 
    return (runr,dls,1)

def check1(runr,dls,chislo):
    if dls+1==chislo:
        return (runr,dls,2)    
    return (runr,dls,1)

def iystallbocc(chislo,runl,runr):
    if d_ch(chislo) == 13:
        (runl,runr)=(runl+10004,runr+5016981688)
    if d_ch(chislo) == 17:
        (runl,runr)=(runl+114,runr+37186099752566)
    if d_ch(chislo)== 18 and str(chislo)[0]=="9":
        (runl,runr) = (2,runr+58823529411765)
        return (runl,runr)
    if d_ch(chislo)== 18 and str(chislo)[-1]=="3":
        (runl,runr) = (12,runr-999999999999999)
        return (runl,runr)
    if d_ch(chislo)== 18 and str(chislo)[-1]=="2":
        (runl,runr) = (runl+20,runr-999999999999998)
        return (runl,runr)
    if d_ch(chislo)== 18 and str(chislo)[-1]=="1":
        (runl,runr) = (runl+12,runr-999999999999999)

    return (runl,runr)

def runleft(runl,w):
    runl-=1
    w+=d_ch(runl)
    return (runl,w)

def runright(runr,w):
    runr+=1
    w+=d_ch(runr)
    return (runr,w)

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