class sloter:
    val = []
    Arp={}

    def __call__(self):
        #pass
        return self
    
    def __init__(self, *fields, default="default"):
        print(fields,"-------------------")
        kostil1 = fields[0]
        kostil2 = fields[1]
        self.Arp = self.Arp.fromkeys(kostil1,kostil2)#.setdefault(kostil2)
        self.default=default
        print(self.Arp,"-----------------------")


    def __delete__(self, num):
        self.Arp[num]=self.default

    def __get__(self, owner):
        return self.Arp[owner]

    def __set__(self):
        print("set srabotal")
        raise AttributeError

    def __iter__(self):
        #for i in self.Arp:
        #    yield self.Arp[i]
        print(self.Arp,"------------iter---------------------")
        return iter(list(self.Arp.values()))

    
s = sloter(("A", "b", "CC"), 100500)()
print(*s)
s.A, s.b, s.CC = 3, 2, 1
print("s.b",s.b,"-----------------------------------")
del s.b
print(*s)
try:
    s.E = 123
    print("---")
except AttributeError:
    print("No .E")