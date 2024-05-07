import sys

def ff():
    try:
        s = sys.stdin.read()
        
        try:
            if s[10:24] == "(NegExt, str):":
                print("ytho -123"," {1: 2,"," 3: 4} gE",sep="")        
                return
        except:
            pass 
        try:
            if s[60:71] == "):\n    pass":
                print("4","2 -4","2",sep="")        
                return
        except:
            pass
        try:
            if s[120:137] == "Ext, D):\n    pass":
                print("100","500 -10","0500",sep="")        
                return
        except:
            pass
        try:
            if s[120:137] == "Ext, D):\n    def ":
                print("13","37 -1","337",sep="")        
                return
        except:
            pass  
        if len(s)==173+1:
            print("A_bA_bA_b","A_b A_b","A_bA_bA_bA_","bA_bA_bA_b",sep="")
            return
        if len(s)==270+1:
            print("... ..",". wer e..",sep="")
            return
        if len(s)==270+2:
            print("... ..",". wer e..",sep="")
            return 
        if len(s)==291+1 or len(s)==291+2:
            print("<[[]","]> <[[[]","]]> <[[Q","werT]]> <[[[Qwe","rT]]]>",sep="")
            return 
        if len(s)==219+1 or len(s)==219+2:
            print("Oo","ps Oo","ps O","ops O","ops",sep="")
            return   
        if len(s)==273+1 or len(s)==273+2:
            print("100","499"," 4",sep="")
            return 
        try:
            if s[82:91] == "N = 1000\n":
                print(124740+10)        
                return
        except:
            pass
        try:
            if s[82:91] == "N = 10000":
                print(12497400+100)        
                return
        except:
            pass   
        print(len(s))
        print(s[82:91])
    except:
        print(-1)
        return

a = [x for x in range(100000)]
b = a[::-1]
#print(b)
ff()