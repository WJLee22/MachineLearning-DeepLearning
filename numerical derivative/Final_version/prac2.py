import numpy as np
import explanation as ex
# 수치미분 예제2(편미분) - 입력변수가 2개인 2변수 함수,
# f(x,y) = 2x + 3xy + y^3 에 대해, f'(1.0, 2.0) 2개의 입력변수인 x,y에 대해 각각 편미분 계산.

# 입력변수 2개인 함수 f(x,y) = 2x + 3xy + y^3 정의.
def func1(input_obj):
    x = input_obj[0]
    y = input_obj[1]
    return (2*x + 3*x*y + np.power(y,3))

# f'(1.0, 2.0) 계산.
input = np.array([1.0, 2.0])
ex.numerical_derivative(func1, input) 