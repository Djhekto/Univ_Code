class MROC3:
    res = {}
    con = 1
    
    def ff(self):
        while 1:
            try:
                s = input()
            except:
                return 'Yes'
            if s.startswith('class '):
                (cls,lg) = self.check(s)
                if lg == 1:
                    name = cls[:cls.find('(')]
                    rewr = [x.strip() for x in cls[cls.find('(') + self.con:-self.con].split(',')]
                    try:
                        temp = [self.res[x].copy() for x in rewr] + [rewr]
                        new_res = self.top(temp)
                    except:
                        return 'No'
                    if new_res:
                        self.res[name] = [name] + new_res
                    else:
                        return 'No'
                else:
                    self.res[cls] = [cls]

    def __init__(self):
        print(self.ff())

    def check(self,str):
        cls = str[6:str.find(':')]
        if '(' in cls:
            lg = 1
        else:
            lg = 0
        return (cls,lg)
    
    @staticmethod
    def asdfg(arr):
        res = []
        for elem in arr:
            res.extend(elem)
        return res

    def top(self, arr):
        otv = []
        while (t := self.asdfg(arr)):
            lg1 = 0
            for cls in t:
                if lg1==1:
                    break
                for k in arr:
                    if cls in k and cls != k[0]:
                        break
                else:
                    otv.append(cls)
                    lg1 = 1
                    for tmp in arr:
                        if cls in tmp:
                            tmp.pop(0)
            else:
                if lg1 == 0:
                    return None
        return otv
    
MROC3()