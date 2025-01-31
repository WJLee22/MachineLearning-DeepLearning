import explanation as ex    
import numpy as np

def my_func2(x):
    return 3*x*(np.exp(x)) # f(x) = 3x * e^x

result = ex.numerical_derivative(my_func2, 2)
print("result =", result) # result = 66.50150507518049


# 지금까지 버전1에서는 입력변수가 하나인 간단한 수치미분을 구현해보았다.

# 하지만 실제 실무에서는, 입력변수가 2개 이상인 다변수 함수에 대한 수치미분을 구현해야 할 경우가 많다.

# 이제부터는 머신러닝 실무코드에서 사용되는 다변수 함수에 대한 수치미분을 코드를 구현해보고자 한다. 