from __future__ import annotations
from inspect import signature
from inspect import get_annotations

def ff(func):
    buf = []
    for i in func.__code__.co_varnames:
        value = signature(func).parameters[i].default
        if isinstance(value, type):
            try:
                defaultcatcher = eval(get_annotations(func)[i])()
#                print(defaultcatcher)
                buf.append(defaultcatcher)
            except:#no def + no value
                buf.append(None)
        else:
            try:
                temp = str(value)
                buf.append(value)
            except:
                pass
    haha = tuple(buf)
    func.__defaults__ = haha
    return func

class init(type):
    def __new__(cls, name, parents, attr):
        for name,elem in attr.items():
#            print(name,elem)
            if isinstance(elem, str):
                pass
            else:
                if elem.__defaults__==None:
                    attr[name]=ff(elem)
                if len(elem.__defaults__)!=elem.__code__.co_argcount-1:
                    attr[name]=ff(elem)
        return type.__new__(cls, name, parents, attr)
