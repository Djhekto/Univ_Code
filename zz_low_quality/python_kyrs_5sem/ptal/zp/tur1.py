import sys

def firstline(str):
#Первая строка — алфавит
#Пустой символ (которым заполнена вся лента) обозначается подчёркиванием ("_")
    #print(str," in first line")
    slovafake = splittoword(str)
    slova = {}
    for i,elem in enumerate(slovafake):
        slova[i] = elem
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
#        try:
#            if komperehoda == "!":
#                break
#        except SyntaxError:
#            pass
#        except:
#            print("vzriiiiiiiiv")
#            return
#s = {0: 'stolbeccifr', 1: 'a', 2: 'b', 3: 'c', 4: '_', 5: '#'}
# s[0]     'stolbeccifr'
# list(s.keys())[list(s.values()).index("a")]       1
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
#Тройка имеет вид C,M,S, где:
    return slovoskotorimrabotaem

def obrabotkagolovki(komanda,komperehoda,kudasmotrim,slovoskotorimrabotaem):
#    logiccccc = 0#debug lishnego sdviga esli udalyaem _
#    if slovoskotorimrabotaem[0]=="_":
#        slovoskotorimrabotaem = slovoskotorimrabotaem[1:]
#        kudasmotrim = 0
#        logiccccc = 1
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
        #sys.exit()
        #slovoskotorimrabotaem[kudasmotrim]=komanda[0]
        # str1 = str[:5] + "#" + str[5+1:]
        #if kudasmotrim>0:
        slovoskotorimrabotaem = slovoskotorimrabotaem[:kudasmotrim] + komanda[0] + slovoskotorimrabotaem[kudasmotrim+1:]
        #if kudasmotrim<=0:
        #    if komanda[0]!=",":
        #        slovoskotorimrabotaem = komanda[0]+slovoskotorimrabotaem
        #    else:
        #        slovoskotorimrabotaem = "_"+slovoskotorimrabotaem[1:]
        #        print(slovoskotorimrabotaem,komanda,kudasmotrim)
        #    kudasmotrim = 1
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
    print("return vzriiiiv")
    return (komanda,komperehoda,kudasmotrim,slovoskotorimrabotaem)


def splittoword(str):
#разделить строку раздел пробелами в список строк
# s = "1 a   3   k,o,o" 
# p = s.split(" ") 
# f = [x for x in p if x!=""] 
# ['1', 'a', '3', 'k,o,o']
    tempp = str.split(" ")
    tempf = [x for x in tempp if x!=""]
    return tempf

    

def checkforinput():
#C — символ алфавита, который надо записать в ячейку
#если он пуст ничего не записывается

    pass

def checkformove():
#M — команда перемещения головки (L — left, N — none, R — right)
#если оно пустo перемещения не происходит

    pass

def checkforstate():
#S — номер состояния, в которое надо перейти после перемещения головки
#если он пуст, состояние не меняется
#остановка MT
 
    pass

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
        print("explode")
        return
    try:
        lineall = lineall.split('\n')
        #print(lineall)
    except:
        print("1 line777")
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
        print("slovoskotorimrabotaem slomalo")
        return
    try:
        lineek = len(lineall)
        #print(lineek, "lini1 chitaya s 0")
    except:
        print("hz skok lini1")
        return
    #print(slovoskotorimrabotaem," <--- slovo in")
    slovoskotorimrabotaem = otherline(lineall,lineek,slova,slov,slovoskotorimrabotaem)
    #print(slovoskotorimrabotaem," <---- slovo out")
    print(slovoskotorimrabotaem)
    
main()



#musor
#    for bykva in range(vsegoiter):#iter bykvi slova
#        kakoiline = 0
#        
#        while 1:#iter po liniyam
#            try:
#                if kakoiline == "!":
#                    break
#            except:
#                pass
#musor      
#    while 1:
#        try:
#            if kakoiline == "!":
#                break
#            if kakoiline>lineek:
#                break
#        except:
#            pass#kakoiline = index  vse norm    
#        line_i = splittoword(lineall[kakoiline])
#        line_i = line_i[1:]#udalyau nomer stroki