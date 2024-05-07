




def f_gen_zamena_init(finit):
    print(finit)
    def ffffffff(*args, **kwargs):
        try:
            print(*args,"--------------",**kwargs)
        except:
            pass
        object = args[0]
        print(object)
        object.data = "hehehhe"
        return 
    return ffffffff


class init(type): 
    def __init__(self, name, bases, dct, **kwargs):
        print("wqewqeqweqweqw")
        print( name, bases, dct)
        print(**kwargs)
        self.__init__ = f_gen_zamena_init(self.__init__)
    
    
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