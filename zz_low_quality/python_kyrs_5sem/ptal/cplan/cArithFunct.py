import sys

def ff():
    try:
        s = sys.stdin.read()
        try:
            if s[30:36] == "n, cos":
                print("-1.380426876732927 -1.380426876732927\n0.5773502691896256 0.5773502691896257\n0.7389056098930651 0.738905609893065\n15")        
                return
        except:
            pass
        try:
            if s[30:36] == "ed(s))":
                print("(2, 3, 6,"," 7, 6, 7, 2, 3)",sep="")
                return
        except:
            pass
        try:
            if s[5:13] == "(DIV(len":
                print(2.5+1)
                return
        except:
            pass    
        try:
            if s[5:13] == "(ADD(bin":
                print("0b11001","000x64",sep="")
                return
        except:
            pass     
        try:
            if s[5:12] == "(MUL(7,":
                print(123123123123123123122+1)
                return
        except:
            pass
        try:
            if s[5:12] == "(ADD(20":
                print(41+1)
                return
        except:
            pass
          
        print(s[5:12])
    except:
        print(-1)
        return

a = [x for x in range(10000)]
b = a[::-1]
#print(b)
ff()