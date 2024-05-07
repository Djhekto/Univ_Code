# метод Зегеля и метод релаксации

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
    
    det_a = np.linalg.det(a)
    print("Определитель матрицы a:", det_a)

    b = np.array([0.560, 0.380, 0.778, 0.749])
    print("вектор b:")
    print(b)
    
    print("\nРЕШЕНИЕ МЕТОДОМ ЗЕЙДЕЛЯ\n")
    x = np.zeros(4)

    for iter in range(10):
        print(f"========{iter+1}=========")
        x_old = x.copy()
        
        for i in range(3, -1, -1):#начинаем с последней строки 4->1 с шагом -1
            print("---------")
            print(f"{a[i, :i]} * {x[:i]} = {np.dot(a[i, :i], x[:i])}" )
            #print("")
            print(f" {b[i]} - {np.dot(a[i, :i], x[:i])} = {(b[i] - np.dot(a[i, :i], x[:i]))}")
            #print("")
            print(f" {(b[i] - np.dot(a[i, :i], x[:i]))} / {a[i, i]} = {(b[i] - np.dot(a[i, :i], x[:i])) / a[i, i]}")
            x[i] = (b[i] - np.dot(a[i, :i], x[:i])) / a[i, i]
        print("Решение системы:", x)
        
        max_diff = np.max(np.abs(x_old - x))
        print(f"Максимальная разница между {x_old} и {x}: {max_diff}")
        
        if (max_diff)<1e-6:
            break


        #if np.allclose(x_old, x, atol=1e-6):
        #    print(f"сошлось на {iter+1} итерации")
        #    break
    
    
    print("\nРЕШЕНИЕ МЕТОДОМ РЕЛАКСАЦИИ\n")
    
    a = np.array([
        [4.238, 0.329, 0.256, 0.425],
        [0.249, 2.964, 0.351, 0.127],
        [0.365, 0.217, 2.897, 0.168],
        [0.178, 0.294, 0.432, 3.701]
    ])
    
    b = np.array([0.560, 0.380, 0.778, 0.749])
    x0 = np.zeros(4)
    
    print(a)
    
    def relax_method(a, b, x0, epsilon=1e-6, max_iterations=100):
        x = x0.copy()
        for ii in range(max_iterations):
            print(f"======={ii+1}========")
            x_new = np.zeros_like(x)
            for i in range(a.shape[0]):
                print(f"{a[i, :i]} * {x[:i]} = {np.dot(a[i, :i], x[:i])} и {a[i, i+1:]} * {x[i+1:]} = {np.dot(a[i, i+1:], x[i+1:])}" )
                print(f"{b[i]} - {np.dot(a[i, :i], x[:i])} - {np.dot(a[i, i+1:], x[i+1:])}" )
                print(f"{b[i] - np.dot(a[i, :i], x[:i]) - np.dot(a[i, i+1:], x[i+1:])} / {a[i, i]}" )
                x_new[i] = (b[i] - np.dot(a[i, :i], x[:i]) - np.dot(a[i, i+1:], x[i+1:])) / a[i, i]
                print(x_new[i],"\n")
                
            if np.linalg.norm(x_new - x) < epsilon:
                print(ii+1,"итераций")
                return x_new
            x = x_new
        print(max_iterations)
        return x
    
    x_1 = relax_method(a, b, x0)
    print("Решение системы:", x_1)
    
    
    
    print(f" | решение методом Зейделя {x} - решение методом Релаксации {x_1} |= \n{abs (x-x_1)}")



main()


























