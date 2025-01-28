import numpy as np
# concatenate메서드로 행렬에 열과 행 추가하기

A = np.array([[10, 20, 30], [40, 50, 60]])
print(A.shape) # (2, 3)

# A matrix에 행(row)으로 추가될 row_add 행렬 정의.
# (3,) 벡터를 -> (1,3) matrix 로 형변환. 가로 벡터
# 벡터는 1차원이기때문에 2차원인 (1,3) matrix로 형변환하여야 함. 
row_add = np.array([70, 80, 90]).reshape(1, 3)

# A matrix에 열(column)으로 추가될 coloumn_add 행렬 정의.
# (2,) 벡터를 -> (2,1) matrix 로 형변환. 세로 벡터
column_add = np.array([1000, 2000]).reshape(2, 1)


#axis는 축을 뜻하는 매개변수로, 
#axis 값에따라서 행렬을 추가하는 방향 축이 달라짐.
# axis=0 : 행을 축으로 연결. 즉, 행이 추가되는 방향인 하단에 추가됨.
# axis=1 : 열을 축으로 연결. 즉, 열이 추가되는 방향인 우측에 추가됨.

# A matrix에 row_add 행렬을 추가한 matrix B 생성. axis값은 0이므로 행을 축으로하여 추가하였으니. 행으로 추가됨.
B = np.concatenate((A, row_add), axis=0)
print(B)

# A matrix에 column_add 행렬을 추가한 matrix C 생성. axis값은 1이므로 열을 축으로하여 추가하였으니. 열로 추가됨.
C = np.concatenate((A, column_add), axis=1)
print(C)
print(C.shape) # (2, 4) 형상으로 변경되었음을 확인할 수 있음. 열이 추가된 것!