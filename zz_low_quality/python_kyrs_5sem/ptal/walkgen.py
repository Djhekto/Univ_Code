def walk2d():
    a = 0
    b = 0
    i1 = yield
    while 1:
        a+=i1[0]
        b+=i1[1]
        yield a, b


g = walk2d()
next(g)
#print(next(g))
while 1:
    (a, b) = eval(input())
    print( g.send((a,b)) )