#Написать метакласс fixed с параметром ndigits (по умолчанию 3),
# в котором все возвращаемые обычными (не статическими и не методами класса) методами значения
# округляются с помощью round() до ndigits знаков после запятой,
# если они вещественные по определению модуля numbers.

from numbers import Real
import inspect

def funround(fun,ndigits):
#    print(fun)
    def kostil1(*args, **kwargs):
        if isinstance(fun(*args, **kwargs), Real):
            try:
                round(fun(*args, **kwargs),ndigits)
            except:
                return fun(*args, **kwargs)
            return round(fun(*args, **kwargs),ndigits)
        else:# если они вещественные по определению модуля numbers == false
            return fun(*args, **kwargs)
    return kostil1

#https://habr.com/ru/post/145835/
class fixed(type): 

    def __new__(cls, name, bases, dct, ndigits=3):
        #print("__new__ srabotal")
        #print(cls,"--",name,"--",bases,"--",dct,"--",ndigits)
        #cls = self;  name = imya;  bases = nasleduemaya fignya;  dct = clovar; 
        # lovim v dct fign1u kotoraya callable
        
        # ne robit
        #for ahahah in dct:
        #    print(ahahah)
        #    if callable(ahahah):
        #        print(ahahah)  
        
        # vrode norm
        #for ahahah in dct:
        #    print(ahahah)
        #    if ahahah.startswith('__') == False:
        #        print(ahahah)
        
        for f in dct:
            #print(dct[f])
            #if f.startswith('__') == False:
            #    try:
            #        dct[f] = funround(dct[f],ndigits)
            #    except:
            #        pass        
            if inspect.isfunction(dct[f]):#https://docs.python.org/3/library/inspect.html
                dct[f] = funround(dct[f],ndigits)
                
        return super(fixed, cls).__new__(cls, name, bases, dct)

