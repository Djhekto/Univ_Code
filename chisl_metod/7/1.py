#метод хорд и метод половинного деления

#from math import sin
import matplotlib.pyplot as plt
import numpy as np
from sympy import symbols, diff,sin

def main():
    def funx(x):
        return x**3 - 0.5 - np.sin(x)

    a = -10
    b = 10

    #решение методом половинного деления

    def check_properties(funx, a, b, eps=1e-5):
        x_values = np.linspace(a, b, 100)
        for x in x_values:
            if np.isnan(funx(x)):
                print(f"функция не является непрерывной на {x}.")
                return False
        
        if funx(a) * funx(b) > 0:
            print(f"функция не меняет знак на интервале [a, b] = {[a,b]}")
            return False
        
        return True

    symbx = symbols('x')
    symbfun = symbx**3 - 0.5 - sin(symbx)
    df = diff(symbfun, symbx)
    print("Производная функции:", df)
    str_df = str(df).replace("cos", "np.cos")
    print(str_df)
    dfunx = eval(f" lambda x: {str_df}")

    if check_properties(funx, a, b):
        print("Функция удовлетворяет условиям метода половинного деления ")
    else:
        return

    def half_interval(a, b):
        return (a + b) / 2

    def polovin_del(a, b, eps = 1e-4):
        itercount = 0
        while abs(b - a) > eps:
            itercount+=1
            c = half_interval(a, b)
            if funx(a) * funx(c) < 0:
                b = c
            else:
                a = c
        print(f"Решение методом половинного деления заняло {itercount+1} итераций")
        return half_interval(a, b)

    resh1 = polovin_del(a, b)
    if resh1 is not None:
        print(f"решение по методу половинного деления = {resh1:.5f}")
    
    # решение методом хорд
    
    def chord_method(x0, dfunx, eps=1e-4, max_iter=100):
        x = x0
        for i in range(max_iter):
            x_new = x - funx(x) / dfunx(x)
            if abs(x_new - x) < eps:
                print(f"решение заняло {i+1} итераций")
                return x_new
            x = x_new
        print(f"решение не сошлось за {max_iter} итераций")
        return None
    
    x0 = 0.5 # Начальное приближение
    root = chord_method(x0,dfunx)
    if root is not None:
        print(f"Решение по методу хорд: {root:.5f}")
    
    # рисуем график
    
    x = np.linspace(a, b, 400)
    y = funx(x)

    plt.plot(x, y)
    plt.title('x**3 - 0.5 - np.sin(x)')
    plt.xlabel('x')
    plt.ylabel('funx(x)')
    plt.show()






main()











