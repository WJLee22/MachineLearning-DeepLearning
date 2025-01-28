import matplotlib.pyplot as plt
import numpy as np

x_data = [ x for x in range(-5,5)]
y_data = np.random.rand(100)

plt.title("Scatter plot")
plt.grid()
plt.plot(x_data, y_data, color='b', marker='o')
plt.show()