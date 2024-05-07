#turtle(coord, direction)
# (0 — восток, 1 — север, 2 — запад, 3 — юг). Координаты увеличиваются на северо-восток.
# "f" (переход на 1 шаг вперёд),
# "l" (поворот против часовой стрелки на 90°)
# "r" (поворот по часовой стрелке на 90°) 
# и возвращает текущие координаты черепахи.

def turtle(coord,direction):
    x = coord[0]
    y = coord[1]
    comm = yield x, y
    while 1:
        #comm = yield
        if comm=="f": 
            match direction:
                case 0: x+=1
                case 1: y+=1
                case 2: x-=1
                case 3: y-=1
        if comm=="r":
            if direction==0: direction = 3
            else:            direction-= 1
        if comm=="l": 
            if direction==3: direction = 0
            else:            direction+= 1
        comm = yield x, y
    
#robo = turtle((0, 0), 0) 
#start = next(robo)
#for c in "flfrffrffr":
#    print(c,*robo.send(c))
#    next(robo)



'''''
def walkd():
    iter(walkd())
def walk2d():
    a = 0
    b = 0
    i1 = yield
    while 1:
        a+=i1[0]
        b+=i1[1]
        yield a, b

r = walk2d()
st = next(r)
print(*r.send((1,1)))
print(*r.send((1,1)))
print(*r.send((1,1)))
'''''

