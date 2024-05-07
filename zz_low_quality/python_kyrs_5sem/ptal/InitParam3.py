
import inspect

def f_gen_zamena_init(cls,finit, tipi,imenatipi):
    print(finit,*tipi,*imenatipi)
    def ffffffff(cls,finit,tipi,imenatipi):
        for i,e in enumerate(tipi):
            print(e,"--------")
            #if is(e,int):
            #    print(e)
            #if e=="int":
            #    print(e)
            #print(type(3))
            if e==type(3):
                print("int")
                #cls.imenatipi[i] = 0
                setattr(cls, imenatipi[i], 0)
            if e==type(range(3)):
                print("range")
                #cls.imenatipi[i] = None
                setattr(cls, imenatipi[i], None)
            if e==list[int]:
                print("list int")
                #cls.imenatipi[i] = []
                setattr(cls, imenatipi[i], [])
            if e==type("[1,2,3]"):
                print("str")
                #cls.imenatipi[i] = "defined"
                setattr(cls, imenatipi[i], "defined")
     
            
                
            #setattr(cls,imenatipi[i],)
        return finit
    return ffffffff(cls,finit,tipi,imenatipi)

class init(type): 
    #def __setitem__(cls,key,value):
    #    cls.key = value
    def __new__(cls, name, bases, dct,*args, **kwargs):
#        try:
#            haha = inspect.get_annotations(cls.__init__)
#            print(haha)
#        except:
#            pass
#        try:
#            print(inspect.get_annotations())#.__init__))
#            print(haha)
#        except:
#            pass
#        try:
#            haha = (inspect.getattr_static(cls.__init__))
#            print(haha)
#        except:
#            pass
        for elem in dct:
            if elem == "__init__":
                ohoho = inspect.get_annotations(dct[elem]).values()
                hohoh = inspect.get_annotations(dct[elem]).keys()                
                dct[elem] = f_gen_zamena_init(cls,dct[elem],ohoho,hohoh)


class C(metaclass=init):
    def __init__(self, var: int, rng: range, lst: list[int], defined: str = "defined"):
        self.data = f"{var}/{rng}/{lst}/{defined}"

c = C()
print(c.data)
c = C(1, range(3))
print(c.data)
c = C(rng=range(4, 7))
print(c.data)
c = C(lst=[1, 2, 3], defined=3)
print(c.data)