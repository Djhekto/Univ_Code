#Написать метакласс init, который рассчитывает на то,
# что методы создаваемого им класса полностью аннотированы. 
# Для каждого позиционного параметра 
# обычного метода в этом классе предусматривается значение по умолчанию
# (если оно не было задано) на основании типа в аннотации.

#Если в аннотации тип параметра простой, значение по умолчанию — это тип_пареметра()

#Если в аннотации тип параметра составной (тип_контейнера[ещё типы], например, list[int]), 
# значение по умолчанию — это тип_контейнера()

#Будем считать что тип самой аннотации 
# при этом всегда types.GenericAlias

#Если объект соответствующего типа
# нельзя создать конструктором без операндов, значение по умолчанию — None

def f_gen_zamena_init(finit):
    print(finit)
    def ffffffff(*args, **kwargs):
        print(*args,"--------------",**kwargs)
        #object = args
        return finit
    return ffffffff

class init(type): 
    def __new__(cls, name, bases, dct,*args, **kwargs):
        print(*args, **kwargs)
        print(cls.__init__)
        print(name.__init__)
        print("+=============++++==++==",cls.__init__.__annotations__)
        print(name.__init__)
        try:
            print(name.data,"+++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        except:
            for elem in dct:
                if elem=="__init__":
                    print("========================================================")
                    #dct[elem] = f_gen_zamena_init(dct[elem])
                    print(name.__init__)
                    dct[elem] = f_gen_zamena_init(cls.__init__)
            
            
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