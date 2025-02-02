import numpy as np
import explanation as ex
# 수치미분 예제3(편미분) - 입력변수가 4개인 4변수 함수,
# f(w,x,y,z) = wx + xyz + 3w + zy^2 에 대해, f'(1.0, 2.0, 3.0, 4.0) 4개의 입력변수인 w,x,y,z에 대해 각각 편미분 계산.

# 입력변수 4개인 함수 f(w,x,y,z) = wx + xyz + 3w + zy^2 정의.
# input_obj는 2x2 행렬. 
def func1(input_obj):
    w = input_obj[0,0]
    x = input_obj[0,1]
    y = input_obj[1,0]
    z = input_obj[1,1]
    return (w*x + x*y*z + 3*w + z*np.power(y,2))

input = np.array([ [1.0, 2.0],[ 3.0, 4.0] ])

# f'(1.0, 2.0, 3.0, 4.0) 계산.
ex.numerical_derivative(func1, input) 