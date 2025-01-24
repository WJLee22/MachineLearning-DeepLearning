import numpy as np

A = np.array([1,2,3])
B = np.array([4,5,6])

# vevtor A,B 출력 
print("A ==", A, ", B ==", B)

# vector A,B 형상 출력 => shape 메서드
print("A.shape ==", A.shape, ", B.shape ==", B.shape)

# vector A,B 차원 출력 => ndim 메서드
print("A.ndim ==", A.ndim, ", B.ndim ==", B.ndim)

# 벡터 산술 연산
print("A + B ==", A + B)
print("A - B ==", A - B)
print("A * B ==", A * B)
print("A / B ==", A / B)