import matplotlib.pyplot as plt
import numpy as np

# list comprehension을 사용하여 x_data, y_data를 생성
# list comprehension은 for문 + 표현식을 이용하여 리스트를 생성하는 방법
x_data = [ x for x in range(-5,5)]
y_data = [ y*y for y in range(-5,5)]

plt.title("line plot")
plt.grid()
# 선형 그래프의 경우 plot()메서드를 사용하면 된다.
plt.plot(x_data, y_data, color='b', marker='o')
plt.show()