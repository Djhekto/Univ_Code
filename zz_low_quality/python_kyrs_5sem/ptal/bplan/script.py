def deleteuntil_n(str,point):
    while 1:
        try:
            if str[point]!="\n":
                str = str[:point] + str[point+1:]
            if str[point]=="\n":
                return str
        except:
            print("net \n posle \t??? | ili EOF (esli 1 raz) -> oba varika dolzni bit1 norm ")
            return str
    


with open(r'D:\ttemp1\python22\ptal\bplan\a.txt', 'r') as infile, \
     open(r'D:\ttemp1\python22\ptal\bplan\b.py', 'w') as outfile:
    data = infile.read()
    
    for i in range(1000):
        ii=str(i)+"	"
        data = data.replace(ii, "")

    data = list(data)
    print(data)
    chl = len(data)
    ch = 0
    while ch<chl:
        if data[ch]=='\t':
#            print(data[ch],"-",end='')
            data = deleteuntil_n(data,ch)
            ch = 0 #kostil1 daze dumat1 len1
            chl = len(data)
        ch+=1
    
    
    
    
#    data = str(data)
#    print(data)
#    data = str(data)
    data = ''.join(str(x) for x in data)
    outfile.write(data)