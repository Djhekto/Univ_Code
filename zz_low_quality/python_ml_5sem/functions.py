from typing import List

#    Вернуть  сумму неотрицательных элементов на диагонали прямоугольной матрицы X. 
#    Если неотрицательных элементов на диагонали нет, то вернуть -1
def sum_non_neg_diag(X: List[List[int]]) -> int: 
    otvet=0
    for e in X:
    	if len(e)==len(X[0]):
            for i in range(len(X[0])):
                if X[i][i] >= 0:
                   otvet+=X[i][i]
            return -1;
    if otvet>0:
        return otvet
    return -1

#    Проверить, задают ли два вектора одно и то же мультимножество.
def are_multisets_equal(x: List[int], y: List[int]) -> bool:
    x.sort()
    y.sort()
    return x==y


#    Вернуть максимальное прозведение соседних элементов в массиве x, 
#    таких что хотя бы один множитель в произведении делится на 3.
#    Если таких произведений нет, то вернуть -1.
def max_prod_mod_3(x: List[int]) -> int:
    otvet=[]
    for i in range(1,len(x)):
        if x[i-1]*x[i]%3==0:
            otvet.append(x[i-1]*x[i])
    if len(otvet)>0:
        return max(otvet) 
    return -1


#    Сложить каналы изображения с указанными весами.
def convert_image(image: List[List[List[float]]], weights: List[float]) -> List[List[float]]:
    pass


#    Найти скалярное произведение между векторами x и y, заданными в формате RLE.
#    В случае несовпадения длин векторов вернуть -1.
def rle_scalar(x: List[List[int]], y:  List[List[int]]) -> int:
    xlist="";ylist="";otvet=[]
    for i in range(len(x)):     xlist+=str(x[i][0])*x[i][1]
    for i in range(len(y)):     ylist+=str(y[i][0])*y[i][1]
    if len(xlist)==len(ylist):
        for i in range(len(xlist)):
            otvet.append(int(xlist[i])*int(ylist[i]))
        return sum(otvet)
    return -1


#    Вычислить матрицу косинусных расстояний между объектами X и Y. 
#    В случае равенства хотя бы одно из двух векторов 0, косинусное расстояние считать равным 1.
def cosine_distance(X: List[List[float]], Y: List[List[float]]) -> List[List[float]]:
    pass
