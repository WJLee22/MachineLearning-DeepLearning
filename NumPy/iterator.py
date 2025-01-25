import numpy as np

A = np.array([[10,20,30,40],[50,60,70,80]]) # 2 x 4 matrix

# 행렬 A의 iterator 생성
it = np.nditer(A, flags=['multi_index'], op_flags=['readwrite'])

# iterator를 이용하여 행렬 A의 모든 원소를 순치적으로 접근.
# it.finished : iterator가 끝에 도달했는지 여부를 반환
while not it.finished:
    # multi_index : iterator가 현재 가리키는 원소의 인덱스를 반환
    idx = it.multi_index

    print("current value => ", A[idx])
    
    # iternext() : iterator가 다음 원소를 가리키도록 이동
    it.iternext()