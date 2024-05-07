import math
import matplotlib.pyplot as plt

# Функция f(x, y)
def f(x, y):
    return (math.exp(2*x)*(2+3*math.cos(x))/(2*y) - 3*y*math.cos(x)/2)

# Начальные условия
a = 1
b = 1.6
x0 = a
y0 = 2
h = 0.0001

listofvalues = []
listofvalues.append((x0,y0))
# Метод Эйлера
while x0 <=b:
    x0 += h
    y1 = y0 + h * f(x0, y0)
    #print(f"x: {x0}, y: {y1}")
    y0 = y1
    listofvalues.append((x0,y0))


x_values = [value[0] for value in listofvalues]
y_values = [value[1] for value in listofvalues]

x0 = a
y0 = 2

# Метод Рунге-Кутты 4-го порядка
listofvalues_rk4 = [(x0, y0)]
while x0 <= b:
    x0 += h
    k1 = h * f(x0, y0)
    k2 = h * f(x0 + 0.5 * h, y0 + 0.5 * k1)
    k3 = h * f(x0 + 0.5 * h, y0 + 0.5 * k2)
    k4 = h * f(x0 + h, y0 + k3)
    y1 = y0 + (1/6) * (k1 + 2*k2 + 2*k3 + k4)
    y0 = y1
    listofvalues_rk4.append((x0, y0))

print("Значение f(b) методом Эйлера", listofvalues[-1])
print("Значение f(b) методом Рунге-Кутты 4-го порядка", listofvalues_rk4[-1])


x_values_rk4 = [value[0] for value in listofvalues_rk4]
y_values_rk4 = [value[1] for value in listofvalues_rk4]



print("Таблица значений метода Эйлера:  Таблица значений метода Рунге-Кутты 4-го порядка:")
print("\tx\ty\t\t\t\t\t\tx \ty")
for i,value in enumerate(listofvalues):
    if i%100!=0:
        continue
    print(f"{i}: {listofvalues[i][0]:.4f}\t{listofvalues[i][1]:.4f}\t\t\t\t\t\t {listofvalues_rk4[i][0]:.4f}\t{listofvalues_rk4[i][1]:.4f}")


print(f"Разница значений в f(b) методом Эйлера и методом Рунге-Кутты для точности {h}")
print(f"x: {x_values_rk4[-1]-x_values[-1]}")
print(f"y: {y_values_rk4[-1]-y_values[-1]}")

# Построение графика
plt.plot(x_values, y_values, label='Метод Эйлера')
plt.plot(x_values_rk4, y_values_rk4, label='Метод Рунге-Кутты 4-го порядка')
plt.xlabel('x')
plt.ylabel('y')
plt.title('График функции, полученной методами Эйлера и Рунге-Кутты 4-го порядка')
plt.legend()
plt.grid(True)
plt.show()