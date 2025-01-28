import numpy as np

# 0~1 사이의 난수 생성.

random_number1 = np.random.rand(3)
random_number2 = np.random.rand(1,3)
random_number3 = np.random.rand(3,1)


print("random_number1 ==", random_number1, ", random_number1.shape ==", random_number1.shape)
print("random_number2 ==", random_number2, ", random_number2.shape ==", random_number2.shape)
print("random_number3 ==", random_number3, ", random_number3.shape ==", random_number3.shape)