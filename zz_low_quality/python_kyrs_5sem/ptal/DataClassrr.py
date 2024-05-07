class Hop:
    flag=0
    Arp={}
    def __init__(self, *fields, default="default"):
        self.Arp.fromkeys(fields).setdefault(default)
        self.default=default

    def __delete__(self, num):
        self.Arp[num]=self.default

    def __get__(self, owner):
        return Hop.Arp[owner]

    def __set__(self, obj, val):
        raise AttributeError

    def __iter__(self):
        for i in self.Arp:
            yield self.Arp[i]
def sloter(fields, default):
    #a=a(fields, default)
    return Hop



s = sloter(("A", "b", "CC"), 100500)()
print(*s)
s.A, s.b, s.CC = 3, 2, 1
del s.b
print(*s)
try:
    s.E = 123
except AttributeError:
    print("No .E")