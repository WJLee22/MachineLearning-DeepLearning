import numpy as np

A = np.array([ [1,2],[3,4],[5,6] ]) # 3 x 2 matrix
B = A.T # A의 전치행렬, 2 x 3 matrix

print("A.shape ==", A.shape, "B.shape ==", B.shape)
print(A) # 3 x 2 matrix 출력
print(B) # 전치된 전치행렬인 2 x 3 matrix 출력
print()
#############################################

# vector 전치행렬

# vector는 행렬이 아닌 1차원 배열형태이기에 전치행렬이 정의되지 않지만,
# 행이나 열이 하나인 행렬로 형변환(reshape)하여 전치행렬을 구할 수 있음.

C = np.array([1,2,3,4,5]) # 5개의 원소를 가지는 vector
D = C.T # C는 vector이기 때문에 C에 대한 전치행렬 정의가 불가능.
# 따라서 C를 (5,1) 형상의 행렬로 형변환 한 후에 전치행렬을 구해야 함.

E = C.reshape(1,5) # (5,) 형상의 벡터 C를 1 x 5 형상의 matrix로 형변환.

# (1 x 5) 1행 5열 형상의 행렬 E를 transpose => 
# 전치행렬 F 도출. F = (5 x 1) 5행 1열 형상의 matrix.
F = E.T 

print("C.shape ==", C.shape, "D.shape ==", D.shape)
print("E.shape ==", E.shape, "F.shape ==", F.shape)
print(F) # 전치행렬 F 출력

