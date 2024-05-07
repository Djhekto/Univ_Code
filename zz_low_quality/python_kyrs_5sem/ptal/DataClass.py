#s = sloter(("A", "b", "CC"), 100500)()
#print(*s)
#s.A, s.b, s.CC = 3, 2, 1
#del s.b
#print(*s)
#try:
#    s.E = 123
#except AttributeError:
#    print("No .E")
#
#100500 100500 100500
#3 100500 1
#No .E  

class sloter:
    val = []
    
    def __init__( self, *args):
        self.names = []
        self.def_ = args[1]
        tupl = args[0]
        print(self.def_,tupl)
        for elem in tupl:
            self.names.append(elem)
            self.__setattr__(elem,self.def_)

    def __setattr__(self, key, value):
        self.__dict__[key] = value
            
    def __call__(self):
        #pass
        return self
     
    def __get__(self, obj, cls):
        return obj._value

    def __delete__(self, obj):
        print(f"Delete from {repr(obj)}")
        obj._value = None
        
    def __set__(self):
        raise AttributeError
    
    def __iter__(self):
        return iter(self.names.get)

    
s = sloter(("A", "b", "CC"), 100500)()
print(*s)
s.A, s.b, s.CC = 3, 2, 1
del s.b
print(*s)
try:
    s.E = 123
    print("---")
except AttributeError:
    print("No .E")