import numpy as np
# numpy.ones()와 numpy.zeros() 함수는 각각 모든 원소가 1 또는 0인 배열을 생성한다.
# 메서드에 작성한 형상의 배열을 생성하고, ones 인지 zeros인지에 따라 모든 원소를 1 또는 0으로 초기화한다.
A = np.ones([3,3])
print("A.shape ==", A.shape, ", A ==", A)

B = np.zeros([3,2])
print("B.shape ==", B.shape, ", B ==", B)