lzetup = []
a = eval(input())

def deleteuntil_n(str,point):
    while 1:
        try:
            if str[point]!="\n":
                str = str[:point] + str[point+1:]
            if str[point]=="\n":
                return str
        except:
            return str

for i in a:
    if type(i) != int:
        [lzetup.append(j) for j in i]
    else:
        if i <= len(lzetup):
            print(tuple(lzetup[:i]))
            lzetup = lzetup[i:]
        else:
            lzetup = deleteuntil_n(lzetup,0)
            break