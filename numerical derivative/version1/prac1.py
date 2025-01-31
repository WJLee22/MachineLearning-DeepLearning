import explanation as ex    
# 수치미분 1차 버전 [예제 1]

# [예제1]
# 함수 f(x) = x^2 에서 미분계수 f'(3)을 구하는 예제.

# 즉 x=3에서 값이 미세하게 변할 때, 함수 f는 얼마나 변하는지를 수치적으로 계산하라는 의미. 

# 미분하고자 하는 대상인 함수 f(x)를 정의. 여기서는 f(x) = x^2
def my_func1(x):
    return x**2

result = ex.numerical_derivative(my_func1, 3)

print("result1 = ", result) # result1 = 6.000000000012662
# x=3에서 미분계수 f'(3)은 약 6.0이라는 것을 알 수 있음.
# 이 6.0이라는 값은, x=3에서 x값이 아주 미세하게 변할 때, 함수 f(x)는 약 6만큼 변한다는 것을 의미함.

# 위와 같은 수치미분을, 실제 수학공식으로 미분계수를 구하여 검증해보면, 
# f(x) = x^2 함수를 미분하면 => f'(x) = 2x 이므로,
# x=3일 때 f'(3) = 6이라는 것을 알 수 있음.

# 이처럼, 수학적 공식으로 계산한 값과 & 수치적으로 계산한 미분 값이 같다는 것을 코드를 통해 확인할 수 있음.