def main():
    lineall=[]
    line = input()
    linelenth = len(line)
    lineall.append(line)
    while 1:
        try:
            line = input()
        except:
            break
        lineall.append(line)
    if lineall[-1]=="":
        lineall = lineall[:-1]
    #print(linelenth,lineall)
    lineall.sort()
    linecount2 = int(len(lineall)/2)
    fakeotv = linelenth-1
    while fakeotv>0:
#        lg = check(lineall,fakeotv,linecount2)
#        if lg=="Y":
#            return fakeotv
#        fakeotv-=1
        spisok = [elem[:fakeotv] for elem in lineall]
        for i in range(linecount2):
            if spisok[2*i]!=spisok[2*i+1]:
                fakeotv = tryjumpcorrect(spisok[2*i],spisok[2*i+1]) 
                break
        else: return fakeotv          
    return "panic"

def check(lineall,fakeotv,linecount2):
    #spisok = []
    #for elem in lineall:
    #    spisok.append(elem[:fakeotv])
    spisok = [elem[:fakeotv] for elem in lineall]
#    spisok.sort()
    for i in range(linecount2):
        #print("+",end = " ")
        if spisok[2*i]!=spisok[2*i+1]:
            fakeotv = tryjumpcorrect(spisok[2*i],spisok[2*i+1])
            return "N"
    #print(spisok)
    return "Y"

def tryjumpcorrect(str1,str2):
    index = len(str1)
    for ii in range(index):
        if str1[ii]!=str2[ii]:
            return ii
    return index

#import time
#start_time = time.time()
print(main())
#print("--- %s seconds ---" % (time.time() - start_time))
