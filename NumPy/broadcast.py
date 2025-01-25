import numpy as np

A = np.array([ [1,2], [3,4] ]) # 2 x 2 matrix
B = 5 # scalar

C = A + B # matrix + scalar => scalar broadcasting. 

# 0차원인 스칼라 B가 2 x 2 matrix로 차원 확장 broadcasting 되어 2 x 2 matrix + 2 x 2 matrix 연산이 수행됨.

print(C)

X = np.array( [ [1,2], [3,4] ] ) # 2 x 2 matrix
Y = np.array( [4,5] ) # 1 x 2 matrix

Z = X + Y # 2 x 2 matrix + 1 x 2 matrix => 1 x 2 matrix가 2 x 2 matrix로 행 크기 확장 broadcasting 되어 2 x 2 matrix + 2 x 2 matrix 연산이 수행됨.

print(Z)