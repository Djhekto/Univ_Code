#import collections
#from time import time

#start_time = time()

#global haha
#haha = 0
#global step; step = -1
#global logic; logic = 0

global location,step
location = 0
step = -1

class Pushpull:
    def __init__(self, loc=0):global location;  location=loc
    def push(self, power=1):  global location;  location+=power
    def pull(self, power=1):  global location;  location-=power
    def __repr__(Pushpull):    return location
    def __str__(Pushpull):
        if location<0:  return f"<{abs(location)}<"
        elif location>0:return f">{location}>"
        return "<0>"
    def __iter__(self):
        global step
        if location<0:
            step = [-elem for elem in list(range(0,abs(location)))]#iter([]))
            return iter(step)
        if location>0:
            step = [elem for elem in list(range(0,location))]
            return iter(step)
        return self
#    def __next__(self):
#        global step
#        print(location)
#        if step: return step.pop(0)
#        raise StopIteration

#N, d = 15000, 101
#x, a, c, m = 6, 1366, 1283, 6075
#line = [Pushpull((x:=(a*x+c)%m)//2%d) for i in range(N)]
#for i in range(N):
#    line[(x:=(a*x+c)%m)%len(line)].push((x:=(a*x+c)%m)%(d//3))
#    line[(x:=(a*x+c)%m)%len(line)].pull((x:=(a*x+c)%m)%(d//3))
#print(sum(v for el in line for v in el))

#print("--- %s seconds ---" % (time() - start_time))

"""
class Pushpull:
    def __init__(self, loc=0): global haha;haha = loc
    def __iadd__(value): global haha;haha += value
    def __isub__(value): global haha;haha -= value
    def push(self, power=1):
        if power>=0: global haha;haha+=power
    def pull(self, power=1): global haha;haha-=power
    def __str__(Pushpull):
        if haha<0: return f"<{abs(haha)}<"
        if haha>0: return f">{haha}>"
        return "<0>"
    def __iter__(self):
        global haha,step
#        print(haha)
#        if haha<0: step = 1
#        if haha>0: step = -1
#        print(step)
        if haha<0: step = 1
        if haha>0: step = -1
        return self
    def __next__(self):
        global haha,step,ii,ii1
        if haha>0:
            if step<haha-1:
                step+=1
                return step
        if haha<0 and step>haha+1:
            step-=1
            return step
        raise StopIteration
"""
#
#===============================================================================
#
"""
import collections
from time import time

start_time = time()

#global haha
#haha = 0
global step; step = -1
global logic; logic = 0

class Pushpull:
    def __init__(self, loc=0): global haha;haha = loc
    def __iadd__(value): global haha;haha += value
    def __isub__(value): global haha;haha -= value
    def push(self, power=1):
        if power>=0: global haha;haha+=power
    def pull(self, power=1): global haha;haha-=power
    def __str__(Pushpull):
        if haha<0: return f"<{abs(haha)}<"
        if haha>0: return f">{haha}>"
        return "<0>"
    def __iter__(self):
#        global haha,step
#        print(haha)
#        if haha<0: step = 1
#        if haha>0: step = -1
#        print(step)
#        if haha<0: step = 1
#        if haha>0: step = -1
        return self
    def __next__(self):
        global haha,step,logic,ii,ii1
        if logic == 0:
            if haha>0: 
                logic = 1
                ii = list(range(0,haha-1))
                return -1
            if haha<0:
                logic = 1
                ii = range(0,haha+1)
                return 1
        if logic == 1:
            while ii:
                return ii.pop(0)  #799515000 #794610000
            logic = 0
#        if haha>0:
#            if step<haha-1:
#                step+=1
#                return step
#        if haha<0 and step>haha+1:
#            step-=1
#            return step
        logic = 0
        raise StopIteration
"""
"""
class Pushpull:
    def __init__(self, loc=0): global haha;haha = loc
    def __iadd__(value): global haha;haha += value
    def __isub__(value): global haha;haha -= value
    def push(self, power=1):
        if power>=0: global haha;haha+=power
    def pull(self, power=1): global haha;haha-=power
    def __str__(Pushpull):
        if haha<0: return f"<{abs(haha)}<"
        if haha>0: return f">{haha}>"
        return "<0>"
    def __iter__(self):
        global haha,step
#        print(haha)
#        if haha<0: step = 1
#        if haha>0: step = -1
#        print(step)
#        if haha<0: step = 1
#        if haha>0: step = -1
        return self
    def __next__(self):
        global haha,step,ii,ii1
        if haha>0:
            if step<haha-1:
                step+=1
                return step
        if haha<0 and step>haha+1:
            step-=1
            return step
        raise StopIteration
"""
"""
class Pushpull:
    def __init__(self, loc=0): # Pushpull & self
#        Pushpull.location=loc
        global haha
        haha = loc
    def __iadd__(value):
        global haha
        haha += value
#        return haha
#        Pushpull.location += value
#        return Pushpull.location
    def __isub__(value):
        global haha
        haha -= value
#        return haha
#        Pushpull.location -= value
#        return Pushpull.location
    def push(self, power=1):
        if power>=0:
            global haha
            haha+=power
#            print(haha)
#            Pushpull.location+=power
    def pull(self, power=1):
        global haha
        haha-=power
#        print(haha)
#        Pushpull.location-=power
#    def __repr__(Pushpull):
#        return  Pushpull.location
    def __str__(Pushpull):
#        if Pushpull.location<0:
#            return f"<{abs(Pushpull.location)}<"
#        elif Pushpull.location>0:
#            return f">{Pushpull.location}>"
#        return "<0>"
#        global haha
        if haha<0:
            return f"<{abs(haha)}<"
        if haha>0:
            return f">{haha}>"
        return "<0>"
    def __iter__(self):
#        if Pushpull.location<0:
        global haha
        global step
        if haha<0:
            step = 1
#        elif Pushpull.location>0:
        if haha>0:
            step = -1
        return self
    def __next__(self):
        global haha,step
#        if Pushpull.location>0 and Pushpull.step<Pushpull.location-1:
        if haha>0 and step<haha-1:
            step+=1
            return step
#        elif Pushpull.location<0 and Pushpull.step>Pushpull.location+1:
        if haha<0 and step>haha+1:
            step-=1
            return step
        raise StopIteration

"""
"""
class Pushpull:
    def __init__(self, loc=0): # Pushpull & self
#        Pushpull.location=loc
        global haha
        haha = loc
    def __iadd__(value):
        global haha
        haha += value
#        return haha
#        Pushpull.location += value
#        return Pushpull.location
    def __isub__(value):
        global haha
        haha -= value
#        return haha
#        Pushpull.location -= value
#        return Pushpull.location
    def push(self, power=1):
        if power>=0:
            pw = power
            global haha
            haha = haha + pw
#            print(haha)
#            Pushpull.location+=power
    def pull(self, power=1):
        global haha
        haha-=power
#        print(haha)
#        Pushpull.location-=power
#    def __repr__(Pushpull):
#        return  Pushpull.location
    def __str__(Pushpull):
#        if Pushpull.location<0:
#            return f"<{abs(Pushpull.location)}<"
#        elif Pushpull.location>0:
#            return f">{Pushpull.location}>"
#        return "<0>"
#        global haha
        if haha<0:
            return f"<{abs(haha)}<"
        if haha>0:
            return f">{haha}>"
        return "<0>"
    def __iter__(self):
#        if Pushpull.location<0:
        global haha
        if haha<0:
            Pushpull.step = 1
#        elif Pushpull.location>0:
        if haha>0:
            Pushpull.step = -1
        return self
    def __next__(self):
#        global haha
#        if Pushpull.location>0 and Pushpull.step<Pushpull.location-1:
        if haha>0 and Pushpull.step<haha-1:
            Pushpull.step+=1
            return Pushpull.step
#        elif Pushpull.location<0 and Pushpull.step>Pushpull.location+1:
        if haha<0 and Pushpull.step>haha+1:
            Pushpull.step-=1
            return Pushpull.step
        raise StopIteration
"""