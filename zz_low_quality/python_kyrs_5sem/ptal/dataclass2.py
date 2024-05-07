class sloter:
    val = []
    global slovar
    slovar = {}

    def __call__(self):
        #pass
        return self
    
    def __init__(self, *fields, **any):
        global slovar
        #print(fields,"-------------------")
        kostil1 = fields[0]
        global kostil2
        kostil2 = fields[1]
        slovar = slovar.fromkeys(kostil1,kostil2)
        #print(slovar,"-----------------------")
        


    def __delattr__(self, num):
        global slovar
        slovar[num]=kostil2
        #print(slovar,"_-----------------------------del")

    def __getattr__(self, owner):
        global slovar
        return slovar[owner]

#    def __set__(self):
#        print("set srabotal")
#        raise AttributeError

    def __setattr__(self, key, value):
        #if self.__dict__[key]:
        global slovar
        kostil3 = list(slovar.keys())
        #print(kostil3,key)
        if key in kostil3:      
            #print(slovar,"----------------------------del prodhel")
            slovar[key] = value
            #print(key)
            self.__dict__[key] = value
        else:
            raise AttributeError


    def __iter__(self):
        global slovar
        #for i in self.slovar:
        #    yield self.slovar[i]
        #print(slovar,"------------iter---------------------")
        return iter(list(slovar.values()))


import random
import string

N, M, T, seed = 100, 1000, 100, 8
random.seed(seed)

sloters, fields = [], []
for k in range(N):
    fields.append(sorted({"".join(random.choices(string.ascii_letters, k=random.randrange(1, 7))) for i in range(M)}))
    sloters.append(sloter(fields[-1], k)())
for k in range(T):
    i = random.randrange(len(sloters))
    sl, attra, attrb = sloters[i], random.choice(fields[i]), random.choice(fields[i])
    attrc = "".join(random.choices(string.ascii_letters, k=random.randrange(1, 7)))
    try:
        r = getattr(sl, attrc)
    except AttributeError:
        r = k
    setattr(sl, attra, getattr(sl, attrb) + r)
for sl in sloters:
    print(*sl)