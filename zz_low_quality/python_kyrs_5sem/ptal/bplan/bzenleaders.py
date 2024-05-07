
mas = []
while 1:
    try:
        cur_str = input().split(' ')
    except:
        break
    if cur_str == ['']:
        break
    time = cur_str[-1].split(':')
    mas.append((cur_str[0], cur_str[1], ' '.join(cur_str[2:-1]), int(time[0]), int(time[1]), int(time[2])))
mas = sorted(mas, key=lambda k: (k[3], k[4], k[5], k[1], k[0], k[2]))

def ff(mas):
    temp = list(mas[0][3:6])
    i = 0
    one = 1
    cur = len(mas)
    for j in range(len(mas[one:])):
        if list(mas[one:][j][3:6]) != temp:
            i += 1
            temp = list(mas[one:][j][3:6])
            if i >= 3:
                cur = j + 1
                break
    mas = mas[:cur]
    return mas

if len(mas) >= 3:
    mas = ff(mas)

end_mas = []

for i in mas:
    end_mas.append([i[0], i[1], i[2], str(i[3]) + ':' + str(i[4]) + ':' + str(i[5])])

len_3 = max([len(i[2]) for i in end_mas])
len_4 = max([len(i[3]) for i in end_mas])
len_1 = max([len(i[0]) for i in end_mas])
len_2 = max([len(i[1]) for i in end_mas])

for i in end_mas:
    print('{0: <{len_1}} {1: <{len_2}} {2: <{len_3}} {3: <{len_4}}'.format(i[0], i[1], i[2], i[3], len_1=len_1, len_2=len_2, len_3=len_3, len_4=len_4))
    