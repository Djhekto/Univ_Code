class MroChecker:	
    mro = {}	
    def __init__(self):	
        while 1:
            try:
                line = input()
            except:
                break#EOF
            if line.startswith('class'):	
                cls = line[6:line.find(':')]	
                if '(' in cls:	
                    cls_name = cls[:cls.find('(')]	
                    cls_decl = [x.strip() for x in cls[cls.find('(') + 1:-1].split(',')]	
                    try:	
                        new_mro = self.build([self.mro[x].copy() for x in cls_decl] + [cls_decl])	
                    except KeyError:	
                        print('No')	
                        break
                    if new_mro:	
                        self.mro[cls_name] = [cls_name] + new_mro	
                    else:	
                        print('No')	
                        break	
                else:	
                    self.mro[cls] = [cls]	
        else:	
            print('Yes')	

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

MroChecker()