# -*- coding=utf8 -*-

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
 
fig = plt.figure()
ax1 = fig.add_subplot(111, projection='3d')

# The coordinates of the anchor point of the bars.
x = np.arange(1,11)
y = np.arange(1,11)
z = np.zeros(10)
print(z)

# The width, depth, and height of the bars, respectively.
dx = np.ones(10)
dy = np.ones(10)
dz = np.arange(10,0,-1)

# Método bar3d para graficar las barras
ax1.bar3d(x, y, z, dx, dy, dz, shade=True)

plt.show()
