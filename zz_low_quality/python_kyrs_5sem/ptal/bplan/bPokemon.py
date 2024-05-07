
def check_int(s):
    try:
        int(s)
        return 1
    except:
        return 0

def ff(otvet,count):
    for i in sorted(otvet):
        if otvet[i] == count:
            print(i)

card_name = {}
people_card = {}
otvet = {}
count = 0

while 1:
    try:
        s1 = input()
    except:
        break
    s1 = s1.split(' / ')
    zro = 0
    if s1 == ['']:
        break
    if check_int(s1[zro]) == 1:
        s1[zro] = int(s1[zro])
        if s1[zro] not in card_name:
            card_name[s1[zro]] = set()
        card_name[s1[zro]].add(s1[1])
    if check_int(s1[zro]) == 0:
        s1[1] = int(s1[1])
        if s1[zro] not in people_card:
            people_card[s1[zro]] = set()
        people_card[s1[zro]].add(s1[1])

for i in people_card.keys():
    cur_set = set()
    for j in people_card[i]:
        cur_set.update(card_name[j])
    temp = len(cur_set)
    otvet[i] = temp
    if temp > count:
        count = temp


ff(otvet,count)