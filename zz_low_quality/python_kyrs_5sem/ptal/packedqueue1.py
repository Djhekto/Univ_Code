#("QWE",1.1,234),2,(None,7),0,2,(7,7,7),2,(12,),(),3,(5,6),3,100500
#
#('QWE', 1.1)
#()
#(234, None)
#(7, 7)
#(7, 7, 12)

#print(eval("(\"QWE\",1.1,234),2,(None,7),0,2,(7,7,7),2,(12,),(),3,(5,6),3,100500"))
#name1 = list(eval("(\"QWE\",1.1,234),2,(None,7),0,2,(7,7,7),2,(12,),(),3,(5,6),3,100500"))
#^
#|____o4en1 creativnoe imya

name1 = list(eval(input()))

#print(name1)
faketuple = []

while 1: 
    name2 = name1.pop(0)
    
    if type(name2) is tuple:    
        faketuple = faketuple + list(name2)
        
    elif type(name2) is int or float:   
        if name2>len(faketuple):    break
        print(tuple(faketuple[:name2]))
        faketuple = faketuple[name2+0:]       

        
#    print("--",faketuple,name2)
