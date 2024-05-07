import random

def ff(x1, y1, x2, y2, x3, y3):
    return x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)

def check(x1, y1, x2, y2, x3, y3):
    return abs(ff(x1, y1, x2, y2, x3, y3))

def check1(x1, y1, x2, y2, yu3, xu3):
    return abs(ff(x1, y1, x2, y2, xu3, yu3))

def randsquare(dot1, dot2):
    (xx1, yy1) = dot1
    (xx2, yy2) = dot2
    counter = 2.0
    yc = (yy1 + yy2) / counter
    xc = (xx1 + xx2) / counter
    xx3 = xc - yy1 + yc
    yy3 = yc + xx1 - xc
    yy4 = yc + xx2 - xc
    xx4 = xc - yy2 + yc
    aaa = sorted([xx1, xx2, xx3, xx4])
    min_x, max_x= aaa[0],aaa[3]
    bbb = sorted([yy1, yy2, yy3, yy4])
    min_y, max_y= bbb[0],bbb[3]    
    #min_x = min(xx1, xx2, xx3, xx4)
    #min_y = min(yy1, yy2, yy3, yy4)
    #max_x = max(xx1, xx2, xx3, xx4)
    #max_y = max(yy1, yy2, yy3, yy4)
    all_1 = check(xx1, yy1, xx2, yy2, xx3, yy3)
    while 1:
        (x, y) = (random.uniform(min_x, max_x), random.uniform(min_y, max_y))
        tt1 = check1(xx1, yy1, xx2, yy2, y, x)
        ss1 = check1(xx1, yy1, x, y, yy3, xx3)
        ff1 = check1(x, y, xx2, yy2, yy3, xx3)
        if all_1 >= ff1 + ss1 + tt1 -0.00001:# skorost1>>>to4nost1
            return (x, y)
        ss2 = check1(xx1, yy1, x, y, yy4, xx4)
        ff2 = check1(x, y, xx2, yy2, yy4, xx4)
        if all_1 >= ff2 + ss2 + tt1 -0.00001:
            return (x, y)
#
#

