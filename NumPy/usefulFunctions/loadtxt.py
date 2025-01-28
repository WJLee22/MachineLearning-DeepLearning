import numpy as np

# loadtxt function
# seperator로 구분된 파일에서 데이터를 읽어오는 함수
loaded_data = np.loadtxt('./data-01.csv', delimiter=',', dtype=np.float32)
 
x_data = loaded_data[ : , 0:-1]
t_data = loaded_data[:, [-1]]

# 데이터 차원 및 shape 확인
print("x_data.ndim = ", x_data.ndim, ", x_data.shape = ", x_data.shape)
print("t_data.ndim = ", t_data.ndim, ", t_data.shape = ", t_data.shape)