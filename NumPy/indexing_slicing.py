import numpy as np

# 요소 6개 짜리 vector 생성 후 2 x 3 matrix로 형변환
A = np.array([ 10, 20, 30, 40, 50, 60 ]).reshape(3,2) 
print("A.shape ==", A.shape)
print(A)
print()

# 예제 1: indexing
print("A[0,0] ==", A[0,0], ", A[0][0] ==", A[0][0]) # 행렬A의 1행 1열에 해당하는 요소인 10 출력
print("A[2,1] ==", A[2,1], ", A[2][1] ==", A[2][1]) # 행렬A의 3행 2열에 해당하는 요소인 60 출력
print()

# 예제 2: slicing
print("A[0:-1, 1:2] ==", A[0:-1, 1:2]) # 행렬A의 1행부터 마지막 행 -1 즉 2행까지, 2열부터 3열까지를 slicing하여 출력
print()

# 예제 3: slicing
print("A[:,0] ==", A[:,0]) # 행렬A의 모든 행의 1열 요소 출력
print("A[:,:] ==", A[:,:]) # 행렬A의 모든 행과 열의 요소 출력