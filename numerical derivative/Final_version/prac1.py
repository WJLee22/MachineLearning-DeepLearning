import numpy as np
import explanation as ex
# 수치미분 예제 - 1변수 함수 f(x) = x^2, f'(3.0) 수치미분 계산

# 입력변수 1개인 함수 f(x) = x^2 정의.
# 입력변수 x는 벡터 및 행렬과 같은 numpy array 객체.
def func1(input_obj):
    x = input_obj[0]
    return x**2

# f'(3.0) 계산. 수치미분 함수 호출
# 매개변수로 func1: 미분하고자 하는 함수, np.array([3.0]): 입력값 3.0을 가지는 벡터.
ex.numerical_derivative(func1, np.array([3.0])) 