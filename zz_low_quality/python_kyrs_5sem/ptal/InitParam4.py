import inspect

class init(type): 
    def __new__(cls, name, bases, dct,*args, **kwargs):
        for elem in dct:
            if elem == "__init__":
                tipi = inspect.get_annotations(dct[elem]).values()
                imya = inspect.get_annotations(dct[elem]).keys()
        ahha = []
        for e in imya:
            ahha.append(e)
        print(ahha)
        for i,e in enumerate(tipi):
            print(e,"--")
            if e==type(3):
                print("int")
                setattr(cls, ahha[i], 0)
            if e==type(range(3)):
                print("range")
                setattr(cls, ahha[i], None)
            if e==list[int]:
                print("list int")
                setattr(cls, ahha[i], [])
            if e==type("[1,2,3]"):
                print("str")
                setattr(cls, ahha[i], "defined")
        print(cls.__dict__)       
        return super(init, cls).__new__(cls, name, bases, dct)
                
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