class MROC3:
    res = {}
    counter = 1

    def __init__(self):
        while 1:
            try:
                s = input()
            except:
                print('Yes')
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


    @staticmethod	
    def join(lsts):	
        ans = []	
        for lst in lsts:	
            ans.extend(lst)	
        return ans	

    def build(self, deps):	
        res = []	
        flag = False	
        while (pars := self.join(deps)):	
            flag = False	
            for cls in pars:	
                if flag:    break
                for lst in deps:	
                    if cls in lst and cls != lst[0]: break
                    else:
                        res.append(cls)
                        flag = True	
                        for tmp in deps:
                            if cls in tmp:
                                tmp.pop(0)
                else:
                    if not flag:
                        return None	
        return res

MROC3()