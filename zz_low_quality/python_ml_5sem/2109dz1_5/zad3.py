#longest_common_prefix(x), которая принимает список строк и возвращает наибольший общий префикс для
#строк в списке строк. Пробельные символы в начале строки не учитывать. Изменять входной список нельзя.
#Если такого префикса нет, требуется вернуть пустую строку. Если на вход поступает пустой список, то следует
#вернуть пустую строку
#

def longest_common_prefix(x):
    if x==[]:
        return ""
    check = isinstance(x, list);
    if check:
        ahah = f1(x)
        return ahah 
    return "ne list"

def f1(x):
    #найти самое короткое слово в списке -> по каждой букве слова чекаем на полное совпадение
    #не совпадает => ретерним что совпало
    otvet =""
    iii=0;www=x[0];
    for i,w in enumerate(x):#индекс чтобы выкинуть наден слово
        if len(w)<len(www):
            www=w; iii=i;
    del x[iii]
    ahahhh=len(www)
    i=0
    for s in www:
       # print(s)
        for w in x:
            ss = w[i]
      #      print(ss)
            if s!=ss:
                return otvet
        otvet=""+otvet+s
        i=i+1
    return otvet        
#main
print(longest_common_prefix(1))
print(longest_common_prefix([]))
print(longest_common_prefix(["asd","asdgg"]))