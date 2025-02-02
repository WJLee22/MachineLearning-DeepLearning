import numpy as np
# 수치미분 최종 버전 설명.

def numerical_derivative(f, x):
    # f: 미분하고자하는 다변수 함수, x: 함수 f의 모든 입력변수를 포함하는 numpy array(벡터 or 행렬)
    delta_x = 1e-4 # 0.0001 (0에 수렴하게 작은 수)
    grad = np.zeros_like(x) # grad 변수는, 입력 파라미터로 들어온 x에 대해서 수치미분을 계산하고 그 결과값을 저장하는 변수인데, x와 형태가 같은 zero배열로 초기화.
    
    it = np.nditer(x, flags=['multi_index'], op_flags=['readwrite']) # x에 대한 iterator 생성. 
    
    # while loop를 이용하여 모든 입력변수에 대한 편미분을 계산
    while not it.finished:
        idx = it.multi_index # iterator의 현재 index를 추출
        
        tmp_val = x[idx] # 원본값 보존을 위해 현재 index의 값을 임시변수에 저장
        
        x[idx] = float(tmp_val) + delta_x 
        fx1 = f(x) # f(x + delta_x) 계산
        
        x[idx] = tmp_val - delta_x
        fx2 = f(x) # f(x - delta_x) 계산
        
        grad[idx] = (fx1 - fx2) / (2*delta_x) # iterator 현재 인덱스 위치의 요소에 대한 편미분 계산
        
        x[idx] = tmp_val # 원본값 복원
        
        it.iternext() # iterator 다음 요소로 이동. 
    
    return grad # 계산된 gradient 반환