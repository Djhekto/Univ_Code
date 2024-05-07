class MROC3:
    res = {}
    counter = 1

    def __init__(self):
        while 1:
            try:
                s = input()
            except:
                break
            if s.startswith('class'):
                temp1 = s.find(':')
                cls = s[6:temp1]
                if '(' in cls:
                    name = cls[:cls.find('(')]
                    dec = [x.strip() for x in cls[cls.find('(') + self.counter:-self.counter].split(',')]
                    try:
                        new_res = self.top([self.res[x].copy() for x in dec] + [dec])
                    except:
                        print('No',"---------------")
                        break
                    if new_res:
                        self.res[name] = [name] + new_res
                    else:
                        print('No',"++++++++++")
                        break
                else:
                    self.res[cls] = [cls]
        else:
            print('Yes')

    @staticmethod
    def union(p):
        val = []
        for k in p:
            val.extend(k)
        return val

    def top(self, arr):	
        res = []
        cnt = 0	
        while 1:
            try:
                t = self.union(arr)
            except:
                break
            cnt = 0
            for cls in t:
                if cnt == 1:
                    break
                for k in arr:	
                    if cls in k and cls != k[0]:
                        break
                else:
                    res.append(cls)	
                    cnt = 1
                    for tmp in arr:
                        if cls in tmp:
                            tmp.pop(0)
            else:
                if cnt == 0:	
                    return None
        return res

MROC3()	