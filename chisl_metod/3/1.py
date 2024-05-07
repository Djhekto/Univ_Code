

#вариант 8 .
# f(x) = e^(-x^j) - (x ^ k) * sin (pi*x^m/2)

from math import sqrt


def createimage():
    import numpy as np
    import matplotlib.pyplot as plt

    def f(x, j, k, m):
        return np.exp(-x**j) - (x**k) * np.sin(np.pi * x**m / 2)

    n = 10000
    a = -2
    b = 2
    j = 2
    k = 3
    m = 4
    x = np.linspace(a, b, n)
    y = f(x, j, k, m)

    sum_f = np.sum(y)
    f_avrg = (1 / (n + 1)) * sum_f
    print(f"Среднее значение функции {f_avrg:.10f} для {n} шагов")

    sum_squares_f = np.sum(y**2)
    f_avrg_squares = (1 / (n + 1)) * sum_squares_f
    print(f"Средний квадрат функции {f_avrg_squares:.10f} для {n} шагов")

    f_avrg_squared = sqrt(f_avrg_squares)
    print(f"Среднеквадратичное число {f_avrg_squared:.10f} для {n} шагов")
    
    positive_count = np.sum(y >=0)
    negative_count = np.sum(y < 0)
    print(f"Кол-во положительных значений {positive_count}, отрицательных {negative_count}")

    f_avr_otklon = np.sqrt(f_avrg_squares - f_avrg**2)
    print(f"Среднеквадратичное отклонение от среднего значения: {f_avr_otklon:.10f} для {n} шагов")

    f_avr_otklon2 = np.sqrt( (1 / (n + 1)) * (np.sum((y - f_avrg)**2) ) )
    print(f"Среднеквадратичное отклонение от среднего значения: {f_avr_otklon2:.10f} по полной формуле")

    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label=r'$f(x) = e^{-x^j} - (x^k) \times \sin\left(\frac{\pi \times x^m}{2}\right)$')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Graph of the function f(x)')
    plt.legend()
    plt.grid(True)
    plt.show()


createimage()


#    f_avr_otklon2 = np.sqrt( (1 / (n + 1)) * (np.sum(y - f_avrg)**2))
#    print(f"Среднеквадратичное отклонение от среднего значения: {f_avr_otklon2} для {n} шагов")