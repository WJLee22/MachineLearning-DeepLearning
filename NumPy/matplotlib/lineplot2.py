import matplotlib.pyplot as plt

x_data = [ -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
y_data = [ -8, -13, -0, 3, 6, -1, -5, -7, 1, 8, 7, 13, 17]

plt.title("line plot2")
plt.grid()
plt.plot(x_data, y_data, color='r', marker='x')
plt.show()     