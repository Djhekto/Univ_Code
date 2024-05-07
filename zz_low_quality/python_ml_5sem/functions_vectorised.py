import numpy as np

#    Вернуть  сумму неотрицательных элементов на диагонали прямоугольной матрицы X. 
#    Если неотрицательных элементов на диагонали нет, то вернуть -1
def sum_non_neg_diag(X: np.ndarray) -> int:
    otvet=0
    d=(np.diag(X))
    if np.all(d<0): return -1
    for i in np.where(d>0):
        otvet+=d[i]
    return sum(otvet)

#    Проверить, задают ли два вектора одно и то же мультимножество.
def are_multisets_equal(x: np.ndarray, y: np.ndarray) -> bool:
    x.sort()
    y.sort()
    return (np.array_equal(x, y))

#    Вернуть максимальное прозведение соседних элементов в массиве x, 
#    таких что хотя бы один множитель в произведении делится на 3.
#    Если таких произведений нет, то вернуть -1.
def max_prod_mod_3(x: np.ndarray) -> int:
    if len(x)>1:
        ahaha= (x*np.concatenate((x[-1:], x[:-1])))[1:]
        logic = ahaha % 3 == 0
        if np.any(logic):
            return np.amax(logic*ahaha)
    return -1


def convert_image(image: np.ndarray, weights: np.ndarray) -> np.ndarray:
    pass

#    Найти скалярное произведение между векторами x и y, заданными в формате RLE.
#    В случае несовпадения длин векторов вернуть -1.
def rle_scalar(x: np.ndarray, y: np.ndarray) -> int:
        xx=x.T
        yy=y.T
        if np.sum(xx[1],axis=0)==np.sum(yy[1],axis=0):
            xl=np.array([])
            for i in range(xx.shape[1]):        xl=np.append(xl,np.array(xx[0,i]*np.ones(x.T[1,i])))
            yl=np.array([])
            for i in range(yy.shape[1]):        yl=np.append(yl,np.array(yy[0,i]*np.ones(y.T[1,i])))
            return int(np.sum(xl*yl))
        return -1


def cosine_distance(X: np.ndarray, Y: np.ndarray) -> np.ndarray:
    pass