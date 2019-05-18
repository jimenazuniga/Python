import numpy as np
import matplotlib.pyplot as plt

# arange recibe el parámetro inicial, el parámetro final
# y el intervalo de incremento.
t = np.arange(0., 5., 0.2)

plt.plot(t, t, 'r--')
plt.plot(t, t**2, 'bs')
plt.plot(t, t**3, 'g^')
#plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')

plt.show()

