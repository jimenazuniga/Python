import numpy as np
import matplotlib.pyplot as plt

country = ("Alemania", "España", "Francia", "Portugal")
position_y = np.arange(len(country))
population = (82.67, 45.56, 66.9, 10.32)

plt.barh(position_y, population, align = "center")

plt.yticks(position_y, country)
plt.xlabel('Población (millones)')
plt.title("Población por país")

plt.savefig("graph.png")
plt.show()
