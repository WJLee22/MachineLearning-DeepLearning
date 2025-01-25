import numpy as np

# dot product: 행렬 간의 곱셈 연산.

# 행렬 곱셈의 조건:
# 행렬 A의 shape이 (m, n) 이고, 행렬 B의 shape이 (n, p) 일 때,
# A의 열 벡터(열의 개수(n))와 B의 행 벡터(행의 개수(n))가 반드시 일치해야 함.
# 곱셈 결과, 행렬 C는 shape이 (m, p) 가 됨.

A = np.array([ [1,2,3],[4,5,6] ])
B = np.array([ [-1, -2],[-3, -4], [-5, -6] ])

# (2 x 3) dot product (3 x 2) = (2 x 2) 행렬.
C = np.dot(A,B)

# matrix A, B 형상 출력 => (2,3), (3,2)
print("A.shape ==", A.shape, "B.shape ==", B.shape)
print("C.shape ==", C.shape)
print(C)