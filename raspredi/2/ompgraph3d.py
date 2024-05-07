import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

x_processes = [1, 2, 4, 8, 16, 32, 64]
y_segments = [100000000, 200000000]
z_time = [[26.826566, 9.305235, 4.724391, 2.291392, 1.121618, 0.525470, 0.244212],
           [49.415730, 18.799150, 8.999815, 4.475489, 2.205053, 1.042899, 0.524470]]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for i, segment in enumerate(y_segments):
    #ax.bar3d(x_processes, [segment] * len(x_processes), np.zeros(len(x_processes)), 1, 1, z_time[i], shade=True)
    ax.scatter(x_processes, [segment] * len(x_processes), z_time[i], c=z_time[i], cmap='viridis')
    
ax.set_xlabel('processes')
ax.set_ylabel('Segments')
ax.set_zlabel('Time')

plt.show()