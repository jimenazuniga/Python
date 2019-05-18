import numpy as np
import matplotlib.pyplot as plt

data = [[72.81, 46.81, 52.4, 11.49], [79.43, 58.51, 57.25, 14.95], [82.67, 66.9, 65.64, 16.62]]
axisX = np.arange(4)
print(axisX+.3)
plt.bar(axisX + 0.0, data[0], color = "b", width = 0.25)
plt.bar(axisX + 0.3, data[1], color = "c", width = 0.25)
plt.bar(axisX + 0.6, data[2], color = "m", width = 0.25)
plt.xticks(axisX+0.25, ["Alemania","Francia","Reino Unido", "Holanda"])


plt.savefig("graph.png")
plt.show()
