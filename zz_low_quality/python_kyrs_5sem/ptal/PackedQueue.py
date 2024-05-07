#("QWE",1.1,234),2,(None,7),0,2,(7,7,7),2,(12,),(),3,(5,6),3,100500
#
#('QWE', 1.1)
#()
#(234, None)
#(7, 7)
#(7, 7, 12)

#eval()
ahha = eval(input())
faketuple = []
while ahha:

       
    if type(ahha) is tuple:
        if ahha != ():
            temp = [elem for elem in ahha]
#            faketuple.append(temp)
            faketuple = faketuple + temp
    
    elif type(ahha) is int or float:
        if ahha>len(faketuple): break
        vivod = tuple(faketuple[:ahha])
        faketuple = faketuple[ahha+1:]       
        print(vivod)
        vivod = ()
    
    print(faketuple)