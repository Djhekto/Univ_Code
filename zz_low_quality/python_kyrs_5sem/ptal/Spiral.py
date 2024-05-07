from collections import Counter


class Spiral:
    
    def __init__(self, s=""):       self.cells = Counter(s)
    def __add__(self, other):       return type(self)(self.cells + other.cells)
    def __sub__(self, other):       return type(self)(self.cells - other.cells)
    def __iter__(self):             return self.cells.elements()
    def __mul__(self, number):      return type(self)(list(self) * number)
    def __rmul__(self, number):     return type(self)(list(self) * number)

    def ff(self):
#        print(*self,"=========================")
        otvet = {}
        fm, fn = [0, 1, 0, -1], [1, 0, -1, 0]
        x = y = n = k = 0
        m1 = m2 = Mx = My = 0
        j = 0
        for ii, c in enumerate(self):
            otvet[x, y] = c
            m1, m2, Mx, My = min(m1, x), min(m2, y), max(Mx, x), max(My, y)
            if ii >= n:
                j = (j + 1) % 4
                k += 1
                n += k
            x, y = x + fm[j], y + fn[j]
        return otvet, (m2, My), (m1, Mx)

    def __str__(self):
        spiral, (m2, My), (m1, Mx) = self.ff()
        ahahah = ""
        hehe = ""
#        print(spiral)
        for j in range(m2, My + 1):
            for i in range(m1,Mx + 1):
#                print(spiral.get((i, j), ' '))
#                ahahah = "".join(spiral.get((i, j), ' '))
                hehe = hehe + spiral.get((i, j), ' ')
#            print(hehe)
            ahahah = ahahah + hehe + "\n"
            hehe = "" 
        ahahah=ahahah[:-1]  
        return ahahah

