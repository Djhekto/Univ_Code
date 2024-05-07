global hahaha
hahaha = "Nuts"

class Nuts():
    def __init__(self, *args):#construct
        pass
    def __setattr__(self, key, value):
        pass
    def __setitem__(self, key, value):
        pass
    def __delitem__(self, key):
        pass
    def __delattr__(self, item):
        pass
    def __getattribute__(self, item):#zadaem novoe pole
        return item
    def __repr__(self, *args, **kwargs):#print
        global hahaha
        return hahaha
    def __getitem__(self, item):#print elem in iter
        return item
    def __iter__(self):#vozvr iter object
        global hahaha
        return iter(hahaha)

#M, N = Nuts(), Nuts(1,2,3,4)
#print(M, N)
#M[100] = N.qwerty = 42
#print(M[100], N.qwerty)
#print(*list(Nuts("QWERQWERQWER")))
#del M["QQ"], N[6:10], M[...], N._, N.qwerty
#print(M.asdfg, N[-2])