import numpy as np
A = np.array([ [1,2,3], [4,5,6] ]) # 2 x 3 matrix A 생성
B = np.array([ [-1,-2,-3], [-4,-5,-6] ]) # 2 x 3 matrix B 생성

# matrix A,B 형상 출력 => shape 속성
# 2행 x 3열 행렬이니깐 (2,3)이 출력됨
print("A.shape ==", A.shape, ", B.shape ==", B.shape)

# matrix A,B 차원 출력 => ndim 속성
# 행렬이니깐 2차원이 출력됨
print("A.ndim ==", A.ndim, ", B.ndim ==", B.ndim)