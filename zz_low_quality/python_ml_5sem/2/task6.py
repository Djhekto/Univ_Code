#я принимает на вход строку – последовательность
#слов, разделенных пробелом и имя файла; слова состоят из строчных и 
# прописных букв латинского алфавита, а разделяются пробельными символами (ввод считать корректным). 
# Функция должна вывести в файл
#для каждого уникального слова в этой строке число его повторений

def check(x: str, file: str):
    x=x.lower()
    #print(x)
    fp = open(file,"w")
    for elem in unique(x.split(" ")):
        fp.write(str(elem+" "))
        #fp.write(str(x.count(" "+elem+" ")))        
        chet=0
        for eheh in x.split(" "):
            if elem==eheh: chet+=1
        fp.write(str(chet))
        fp.write("\n")

def unique(list1):
    unique_list = []
    for x in list1:
        if x not in unique_list:
            unique_list.append(x)
    return unique_list

    

#check("swfwef wnepfnwpen ewpofnwenk","hehe.txt")
#check("a aa abC aa ac abc bcd a", "file.txt")
check("a A a", "file.txt")

check("c c f d aaA a c d r c ccc cC c b b b b", "file.txt")
