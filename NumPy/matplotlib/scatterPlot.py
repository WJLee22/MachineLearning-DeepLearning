import matplotlib.pyplot as plt
import numpy as np

x_data = np.random.rand(100)
y_data = np.random.rand(100)

plt.title("Scatter plot") # 그래프 제목
plt.grid() # xy축 격자무늬.그리드 표시

# 그래프의 종류, 색상, 마커를 설정하여 출력
# 그래프의 종류: scatter(산점도). 다른 종류로는 plot(선그래프), bar(막대그래프) 등이 있다.
# x축, y축 데이터: x_data, y_data
# 색상: color='b'는 파란색, color='r'은 빨간색, color='g'는 초록색
# 데이터 마커: marker='o'는 원형, marker='x'는 x표시, marker='*'는 별표시
plt.scatter(x_data, y_data, color='b', marker='o')
plt.show() # 그래프 출력