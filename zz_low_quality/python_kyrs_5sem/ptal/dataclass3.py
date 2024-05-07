class sloter:
    val = []
    slovar = {}
    initsw = 0

    def __call__(self):
        return self
    
    def __init__(self, *fields, **any):
        kostil1 = fields[0]
        global kostil2
        kostil2 = fields[1]
        self.slovar = self.slovar.fromkeys(kostil1,kostil2)
        #print("init",self.slovar)
        self.initsw = 1
        del self.slovar['initsw']
        #print(self.slovar)

    def __delattr__(self, num):
        self.slovar[num]=kostil2

    def __getattr__(self, owner):
        try:
            return self.slovar[owner]
        except:
            raise AttributeError

        #print(self.slovar,self.slovar[owner])
        #return self.slovar[owner]
        #if self.slovar[owner]:
        #    return self.slovar[owner]
        #else:
        #    raise AttributeError

    def __setattr__(self, key, value):
        if self.initsw == 0:
            self.slovar[key] = value
            self.__dict__[key] = value
        else:
            kostil3 = list(self.slovar.keys())
            if key in kostil3:      
                self.slovar[key] = value
                self.__dict__[key] = value
            else:
                raise AttributeError


    def __iter__(self):
        return iter(list(self.slovar.values()))

