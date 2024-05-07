import sys

class MROC3:
    otvet = {}
    con =1

    def __init__(self):
        temp = self.ff()
        print(temp)

    def ff(self):
        while 1:
            try:
                s = input()
            except:
                return 'Yes'
            (cls,lg) = self.check(s)
            if lg == 1:
                name = cls[:cls.find('(')]
                dec = [x.strip() for x in cls[cls.find('(') + self.con:-self.con].split(',')]
                try:
                    temp = [self.otvet[x].copy() for x in dec] + [dec]
                    new_res = self.top(temp)
                except:
                    return 'No'
                if new_res:
                    self.otvet[name] = [name] + new_res
                else:
                    return 'No'
            if lg==0:
                self.otvet[cls] = [cls]
    
    def check(self,str):
        if str.startswith('class'):
            return (0,2)
        cls = str[6:str.find(':')]
        if '(' in cls:
            lg = 1
        else:
            lg = 0
        return (cls,lg)

    @staticmethod
    def onion(arr):
        otv = []
        for elem in arr:
            otv.extend(elem)
        return otv

    def top(self, arr):
        res = []
        lg1 = 0
        while 1:
            try:
                t1 = self.onion(arr)
            except:
                return res
            lg1 = 0
            for cls in t1:
                if lg1==1:
                    break
                for k in arr:
                    if cls in k and cls != k[0]:
                        break
                else:
                    res.append(cls)
                    lg1 = 1
                    for tmp in arr:
                        if cls in tmp:
                            tmp.pop(0)
            else:
                if lg1 == 0:
                    return None


MROC3()