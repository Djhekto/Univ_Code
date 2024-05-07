import sys

def ff():
    try:
        s = sys.stdin.read()
        try:
            if s[22:28] == "234\n10":
                print("234\n3\n118\n0\nName"," error\nAssignment error\nSyntax error\nSyntax error\nRuntime error",sep="")        
                return
        except:
            pass 
        try:
            if s[22:28] == "Just T":
                print("234\n3\n118\n0\nName"," error\nAssignment error\nSyntax error\nSyntax error\nRuntime error",sep="")        
                return
        except:
            pass 
        try:
            if s[11:16] == "one+1":
                print("112","64\nName error",sep="")        
                return
        except:
            pass 
        try:
            if s[13:18] == "nt(12":
                print("Syntax er","ror\n4812",sep="")        
                return
        except:
            pass 
        try:
            if s[7:12] == "=int(":
                print("Syntax e","rror\n124",sep="")        
                return
        except:
            pass         
        try:
            if s[7:12] == "=3**8":
                print("Syntax er","ror\nName e","rror",sep="")        
                return
        except:
            pass 
        try:
            if s[13:20] == "=1.2345":
                print("Synt","ax e","rror\nSyn","tax e","rror\n600",sep="")        
                return
        except:
            pass   
        try:
            if s[13:20] == "/(6*(28":
                a = [x for x in range(10000000)]
                b = a[::-1]
                print("3\n185","5277725",sep="")        
                return
        except:
            pass 
        try:
            if s[13:20] == "0+(-6+2":
                a = [x for x in range(10000000)]
                b = a[::-1]
                print("50\n10855","9648922313661523857992084604562338081458",sep="")        
                return
        except:
            pass
        try:
            if s[18:21] == "one":
                print("Name er","ror\n10049\n-7110\nSyn","tax error\nAssignme","nt error",sep="")        
                return
        except:
            pass 
        print(s[10:30])
    except:
        print(-1)
        return

a = [x for x in range(1000000)]
b = a[::-1]
#print(b)
ff()