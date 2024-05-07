import numpy as np
import math


def main():
    a = np.array([
        [4.238, 0.329, 0.256, 0.425],
        [0.249, 2.964, 0.351, 0.127],
        [0.365, 0.217, 2.897, 0.168],
        [0.178, 0.294, 0.432, 3.701]
    ])
    print("Матрица:")
    print(a)

    b = np.array([0.560, 0.380, 0.778, 0.749])
    print("вектор b:")
    print(b)
    
    h = 0.01

    print("\nРЕШЕНИЕ МЕТОДОМ ГАУСА\n")

    # Проверка, является ли матрица невырожденной
    if np.linalg.det(a) != 0:
        a_inv = np.linalg.inv(a)
        print("Определитель не равен нулю. Решение существует")
        print("Обратная матрица:")
        print(a_inv)
    else:
        print("Матрица вырожденная, обратная матрица не существует, решение не является единственным")
        return

    a_norm = np.linalg.norm(a)
    a_inv_norm = np.linalg.norm(a_inv)
    b_norm = np.linalg.norm(b)

    print(f"Норма матрицы A: {a_norm:.8f}")
    print(f"Норма обратной матрицы A^{-1}:, {a_inv_norm:.8f}")
    print(f"Норма вектора b:, {b_norm:.8f}")

    absp_b = 0.001
    otnp_b = absp_b/b_norm
    print("относительная погрешность вектора b:", otnp_b)
    #Находим погрешности решения по норме матрицы, обратной матрицы и вектора б
    absp_a = a_inv_norm*absp_b
    otnp_a = a_inv_norm*a_norm*otnp_b
    
    # Приведение матрицы к верхнему треугольному виду
    for i in range(3):#Цикл по строкам матрицы с первой до предпоследней строки
        for j in range(i+1, 4):#Цикл по всем столбцам матрицы 
            factor = a[j, i] / a[i, i]
            #print(factor)
            a[j] = a[j] - factor * a[i]
            b[j] = b[j] - factor * b[i]

#    np.set_printoptions(precision=7, suppress=True, formatter={'float_kind': zero_formatter})
#    def zero_formatter(x):
#        if x <= 0.00000001:
#            return '0'
#        else:
#            return '{:.7f}'.format(x)

#    np.set_printoptions(formatter={'float_kind': zero_formatter})

    np.set_printoptions(precision=7, suppress=True)
    print("Треугольный вид Матрицы:")
    print(a)

    # Решение системы уравнений обратной подстановкой
    x = np.zeros(4)
    x[3] = b[3] / a[3, 3]
    for i in range(2, -1, -1):
        x[i] = (b[i] - np.dot(a[i, i+1:], x[i+1:])) / a[i, i]

    print("Решение системы уравнений методом Гаусса:", x)
    print(f" абслоютная погрешность A: {absp_a:.8f}\n относительная прогешность А: {otnp_a:.8f}")


    print("\nРЕШЕНИЕ МЕТОДОМ ПРОСТОЙ ИТЕРАЦИИ\n")
    
    a = np.array([
        [4.238, 0.329, 0.256, 0.425],
        [0.249, 2.964, 0.351, 0.127],
        [0.365, 0.217, 2.897, 0.168],
        [0.178, 0.294, 0.432, 3.701]
    ])
    b = np.array([0.560, 0.380, 0.778, 0.749])
    x0 = np.zeros(4)

    max_elements = np.max(a, axis=1)
    bb = a / max_elements[:, np.newaxis]
    print(f"матрица B\n {bb}")
    bb[bb == 1] = 0
    bb = -bb
    print(f"матрица B\n {bb}")
    
    c = b / max_elements
    print("c:", c)
    
    bb_norm = np.linalg.norm(bb)
    print(f"Норма матрицы B: {bb_norm:.8f}")

    c_norm = np.linalg.norm(c)
    print(f"Норма c: {c_norm:.8f}")

    x1 = bb * x0 + c
    eps = 0.001
    
    #k = math.floor(math.log((np.linalg.norm(x1)+eps)*(1-bb_norm)) / math.log(bb_norm)) + 1
    k = math.floor(math.log(eps*(1-bb_norm)/(np.linalg.norm(x1)) ) / math.log(bb_norm)) + 1
    print(f"k : {k} = [ {math.log(eps*(1-bb_norm)/(np.linalg.norm(x1)) )} / { math.log(bb_norm) } ]")


    def simple_iteration(A, b, x0, h, max_iterations, tolerance):
        x = x0
        x_old = x0
        itercount = -1
        for i in range(max_iterations):
            x_new = x - h * np.dot(A, x) + h * b
            itercount = i
            if np.linalg.norm(x_new - x) < tolerance:
                break
            x_old = x
            x = x_new
            print(f"iter {i+1}: x = {x}")
        return x,x_old
    
    x,x_old = simple_iteration(a, b, x0, 0.1,k, eps)
    print("Решение системы уравнений методом простой итерации:", x, "для количества итераций", k)
    
    absp_mpi = (bb_norm / (1 - bb_norm) )* np.linalg.norm((x - x_old))
    print("Абсолютная погрешность решения методом простой итерации:", absp_mpi)




main()










































































