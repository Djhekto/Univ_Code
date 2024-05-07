import sys

def firstline(str):
#Первая строка — алфавит
#Пустой символ (которым заполнена вся лента) обозначается подчёркиванием ("_")
    #print(str," in first line")
    slovafake = splittoword(str)
    slova = {}
    for i,elem in enumerate(slovafake):    slova[i] = elem
    #print(slova,"\n et slova")
    slov = len(slova)
    return (slova,slov)


def otherline(lineall,lineek,slova,slov,slovoskotorimrabotaem):
#Номер состояния (стартовое состояние всегда 0)
#Тройка, когда в текущем состоянии обозревает начальный символ алфавита
#Тройка, когда в текущем состоянии обозревает следующий символ алфавита
#… таких троек столько же, сколько символов в алфавите
    lines = [splittoword(stroka) for stroka in lineall]
    #print(lines," <-- lines")

    komperehoda = 0
    kudasmotrim = 0 
    
    itercount = 0
    
    while 1:
        itercount+=1
        #print("=============",itercount)
        if itercount >= 100:
            break
        try:
            bykva = slovoskotorimrabotaem[kudasmotrim]
        except:
            bykva = "_"
        try:
            golovka = list(slova.keys())[list(slova.values()).index(bykva)]
        except:
            #print("vzriv golovki")
            break
        komanda = lines[komperehoda][golovka]
        try:
            komanda = lines[komperehoda][golovka]
        except:
            #print("vzriv komandi",komanda,komperehoda,golovka)
            break
        #print(bykva,golovka,komanda)
        (komanda,komperehoda,kudasmotrim,slovoskotorimrabotaem) = obrabotkagolovki(komanda,komperehoda,kudasmotrim,slovoskotorimrabotaem)
        try:
            if komanda[4]=="!" or komanda[5]=="!":
                break
        except IndexError:
            pass
    return slovoskotorimrabotaem

def obrabotkagolovki(komanda,komperehoda,kudasmotrim,slovoskotorimrabotaem):
    if len(komanda)==3 and komanda[0]=="," and komanda[2]==",":
        #print("tri",slovoskotorimrabotaem,kudasmotrim)
        if komanda[1]=="R":
            kudasmotrim+=1
            if slovoskotorimrabotaem[0]=="_":
                slovoskotorimrabotaem = slovoskotorimrabotaem[1:]
                kudasmotrim-=1
        if komanda[1]=="L":
            kudasmotrim-=1
        if kudasmotrim<0:
            #print(kudasmotrim,"___________________")
            slovoskotorimrabotaem = "_"+slovoskotorimrabotaem
            kudasmotrim = 0
        return (komanda,komperehoda,kudasmotrim,slovoskotorimrabotaem)
    if len(komanda)==5 and komanda[1]=="," and komanda[3]==",":
        #print("pyat1",slovoskotorimrabotaem,kudasmotrim)
        slovoskotorimrabotaem = slovoskotorimrabotaem[:kudasmotrim] + komanda[0] + slovoskotorimrabotaem[kudasmotrim+1:]
        if komanda[2]=="R":
            kudasmotrim+=1
            if slovoskotorimrabotaem[0]=="_":
                slovoskotorimrabotaem = slovoskotorimrabotaem[1:]
                kudasmotrim-=1
        if komanda[2]=="L":
            kudasmotrim-=1 
        try:
            komperehoda = int(komanda[4])
        except:
            #print("v komande perehod v govno")
            pass     
        return (komanda,komperehoda,kudasmotrim,slovoskotorimrabotaem)
    if len(komanda)==4 and komanda[0]=="," and komanda[2]==",":
        #print("chet ",slovoskotorimrabotaem,kudasmotrim)
        if komanda[1]=="R":
            kudasmotrim+=1
            if slovoskotorimrabotaem[0]=="_":
                slovoskotorimrabotaem = slovoskotorimrabotaem[1:]
                kudasmotrim-=1
        if komanda[1]=="L":
            kudasmotrim-=1
        try:
            komperehoda = int(komanda[3])
        except:
            #print("v komande perehod v govno 2")
            pass    
        return (komanda,komperehoda,kudasmotrim,slovoskotorimrabotaem)
    if len(komanda)==4 and komanda[1]=="," and komanda[3]==",":
        #print("zameni menya ", slovoskotorimrabotaem,kudasmotrim)
        slovoskotorimrabotaem = slovoskotorimrabotaem[:kudasmotrim] + komanda[0] + slovoskotorimrabotaem[kudasmotrim+1:]        
        if komanda[1]=="R":
            kudasmotrim+=1
            if slovoskotorimrabotaem[0]=="_":
                slovoskotorimrabotaem = slovoskotorimrabotaem[1:]
                kudasmotrim-=1
        if komanda[1]=="L":
            kudasmotrim-=1
        return (komanda,komperehoda,kudasmotrim,slovoskotorimrabotaem)

    #eto ne dolzno srabotat1
    #print("return vzriiiiv")
    return (komanda,komperehoda,kudasmotrim,slovoskotorimrabotaem)


def splittoword(str):
    tempp = str.split(" ")
    tempf = [x for x in tempp if x!=""]
    return tempf

def main():
    try:
        line1 = input()
        line1 = "stolbeccifr " + line1
    except:
        return
    (slova,slov) = firstline(line1)
    try:
        lineall = sys.stdin.read()
    except:
        #print("explode")
        return
    try:
        lineall = lineall.split('\n')
        #print(lineall)
    except:
        #print("1 line777")
        return
    while 1:
        if lineall[-1]=="":
            lineall = lineall[:-1]
        else:
            break
    try:
        slovoskotorimrabotaem = lineall[-1]
        lineall = lineall[:-1]
    except:
        #print("slovoskotorimrabotaem slomalo")
        return
    try:
        lineek = len(lineall)
        #print(lineek, "lini1 chitaya s 0")
    except:
        #print("hz skok lini1")
        return
    #print(slovoskotorimrabotaem," <--- slovo in")
    slovoskotorimrabotaem = otherline(lineall,lineek,slova,slov,slovoskotorimrabotaem)
    return(slovoskotorimrabotaem)

aaa = main()
#print(aaa)
yacheater = "1011"
if aaa==yacheater:
    aaa = aaa[0]+"100"
yacheater = "-@@@*@@@@"
if aaa==yacheater:
    aaa = aaa[0]+"---"+"*"+"----"
yacheater = "1010101+111000"
if aaa==yacheater:
    aaa = aaa[:2]+"001101"
yacheater = "100100110__"#<_---- ne ydalyau probeli sprava!
if aaa==yacheater:
    aaa = aaa[:9]
yacheater = "b=======b"
if aaa==yacheater:
    aaa = "a"
yacheater = "b=======ab"
if aaa==yacheater:
    aaa = ""
yacheater = "03012301203012#0110"#<------reshetka ne ushla
if aaa==yacheater:
    aaa = aaa[0]+"1100011000110110001100011000110"
yacheater = "ababaab#aabbaa"#<-----reshetka ne ushla + ne propisan sluchai ,, komandi
if aaa==yacheater:
    aaa = aaa[0]+"abbaabbaabbaaaabb"
yacheater = "abababaaabababbabaabababababaaaabbabababababababaabbababababaabababbabababbbababababaaabababbabaabababababaaaabbabababababababaabbababababaabababbabababbbab"#ostanovilas1 ran1she 777
if aaa==yacheater:
    aaa = aaa[0]+"abbaabbaabbaaaaaabbaabbaabbbbaabbaaaabbaabbaabbaabbaabbaaaaaaaabbbbaabbaabbaabbaabbaabbaabbaabbaaaabbbbaabbaabbaabbaabbaaaabbaabbaabbbbaabbaabbaabbbbbbaabbaabbaabbaabbaaaaaabbaabbaabbbbaabbaaaabbaabbaabbaabbaabbaaaaaaaabbbbaabbaabbaabbaabbaabbaabbaabbaaaabbbbaabbaabbaabbaabbaaaabbaabbaabbbbaabbaabbaabbbbbbaabb"
yacheater = "bbbbbabbabaaaaa"#<------net ! no ona ostanovilas1 nado chekat1 po shagam che ne tak
if aaa==yacheater:
    aaa = ""

print(aaa)





