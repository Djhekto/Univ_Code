#числ реш опр интегр
# м трапец м симпсона м ньютона-лейбница

from math import sqrt

from sympy import Symbol, diff, cos, lambdify
import numpy as np


def main():

    def f(x):
        return x * np.cos(2 * x)

    a = 0
    b = 1
    eps = 0.001

    symbx = Symbol("x")
    smyfunx = lambdify(symbx, symbx*cos(2*symbx), "sympy")
    sddf = diff(diff(smyfunx(symbx), symbx), symbx)
    print("Вторая производная по х\n",sddf)
    sddf_func = lambdify(symbx, abs(sddf), "numpy")
    
    x_values = np.linspace(a, b, 1000)
    sddf_values = sddf_func(x_values)
    M = np.max(sddf_values)
    print("Максимум второй производной на интервале:", M)
    
    h = sqrt(  (12*eps) / (M*abs(b-a))  )
    print("шаг",h)
    h2 = h*2


    print("\nМетод трапеций")

    def trapezoidal_rule(a, b, h, f):
        n = int((b - a) / h)
        print("точек", n)
        x = a
        integral = 0.5 * (f(a) + f(b))
        for i in range(1, n):
            x += h
            integral += f(x)
        integral *= h
        return integral

    integral_m_trapez = trapezoidal_rule(a, b, h, f)
    print(f"Интеграл функции x*cos(2x) на интервале [{a}, {b}] с шагом {h}:\n{ integral_m_trapez}")
    integral_m_trapez2 = trapezoidal_rule(a, b, h2, f)
    print(f"h*2 :\n{ integral_m_trapez2}")
    print("Погрешность метода по правилу Рунге", abs(integral_m_trapez- integral_m_trapez2)/3)


    print("\nМетод Симпсона")

    def simpsons_rule(a, b, h, f):
        n = int((b - a) / h)
        print("точек", n)
        integral = f(a) + f(b)
        for i in range(1, n):
            x = a + i * h
            if i % 2 == 0:
                integral += 2 * f(x)
            else:
                integral += 4 * f(x)
        integral *= h / 3
        return integral

    integral_simpson = simpsons_rule(a, b, h, f)
    print(f"Интеграл функции x*cos(2x) на интервале [{a}, {b}] с шагом {h} методом Симпсона:\n{integral_simpson}")
    integral_simpson2 = simpsons_rule(a, b, h2, f)
    print(f"h*2:\n{integral_simpson2}")
    print("Погрешность метода по правилу Рунге", abs(integral_simpson- integral_simpson2)/15)


    print("\nМетод Ньютона-Лейбница")

    def newton_leibniz_rule(a, b, h, f):
        n = int((b - a) / h)
        print("точек", n)
        integral = 0
        for i in range(n):
            x = a + i * h
            integral += f(x) * h
        return integral

    integral_newton_leibniz = newton_leibniz_rule(a, b, h, f)
    print(f"Интеграл функции x*cos(2x) на интервале [{a}, {b}] с шагом {h} методом Ньютона-Лейбница:\n{integral_newton_leibniz}")
    integral_newton_leibniz2 = newton_leibniz_rule(a, b, h2, f)
    print(f"h*2:\n{integral_newton_leibniz2}")
    print("Погрешность метода по правилу Рунге", abs(integral_newton_leibniz - integral_newton_leibniz2)/15)


    return

main()
