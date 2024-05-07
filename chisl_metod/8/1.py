# ЧМ решения систем нелинейных уравнений
# мпи Зейделя Ньютона Exel

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def main():
    def funx1(x1,x2):
        return np.cos(x1+x2) + 2*x2
    
    def funx2(x1,x2):
        return x1 + np.sin(x2) -0.6
    
    a = -10
    b = 10
    
    # Create a grid of points
    x1 = np.linspace(a, b, 100)
    x2 = np.linspace(a, b, 100)
    x1, x2 = np.meshgrid(x1, x2)
    
    # Calculate the values of the functions at each point
    z1 = funx1(x1, x2)
    z2 = funx2(x1, x2)
    
    # Create a 3D plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    # Plot the first function
    ax.plot_surface(x1, x2, z1, alpha=0.5, rstride=100, cstride=100)
    
    # Plot the second function
    ax.plot_surface(x1, x2, z2, alpha=0.5, rstride=100, cstride=100)
    
    # Set labels
    ax.set_xlabel('x1')
    ax.set_ylabel('x2')
    ax.set_zlabel('f(x1, x2)')
    
    # Show the plot
    plt.show()
    
    def simple_iteration(x1_init, x2_init, max_iter=100, eps=1e-6):
        x1, x2 = x1_init, x2_init
        for i in range(max_iter):
            x1_new = x1 - funx1(x1, x2) / (np.cos(x1+x2) - 2)
            x2_new = x2 - funx2(x1, x2) / (1 - np.sin(x2))
            
            if np.abs(x1_new - x1) < eps and np.abs(x2_new - x2) < eps:
                break
            
            x1, x2 = x1_new, x2_new
        
        return x1, x2

    # Начальное приближение
    x1_init, x2_init = 0, 0

    # Решение системы уравнений
    x1_sol, x2_sol = simple_iteration(x1_init, x2_init)

    print(f"Решение системы уравнений: x1 = {x1_sol}, x2 = {x2_sol}")

main()
































