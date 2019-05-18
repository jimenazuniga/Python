from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

# Se crea la figura
fig = plt.figure()

# Se agrega un plano 3D
ax1 = fig.add_subplot(111,projection='3d')

# Primer vector 3D
x = np.arange(1, 11)
y = np.arange(1, 11)
z = np.arange(1, 11)

# Segundo vector 3D
x2 = np.arange(-1, -10, -1)
y2 = np.arange(-1, -10, -1)
z2 = np.arange(1, 10, 1)

# Se grafican los vectores
ax1.scatter(x, y, z, c='b', marker='o')
ax1.scatter(x2, y2, z2, c ='g', marker='^')
plt.show()

