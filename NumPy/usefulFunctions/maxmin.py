import numpy as np

# 벡터의 최대값, 최소값, 최대값의 인덱스, 최소값의 인덱스
X = np.array([2,4,6,8])

print(f"np.max(X) == {np.max(X)}")
print("np.min(X) == {}".format(np.min(X)))
print("np.argmax(X) ==", np.argmax(X))
print("np.argmin(X) ==", np.argmin(X))   

# 행렬의 최대값, 최소값, 최대값의 인덱스, 최소값의 인덱스
# 행렬의 경우, axis를 지정하여 행 또는 열 단위로 계산한다. 
# axis=0: 열을 축으로 계산, axis=1: 행을 축으로 계산
X = np.array([[2,4,6], [1,2,3], [0,5,8]])

print("np.max(X) ==", np.max(X, axis=0)) # 각 열의 최대값을 모아서 벡터로 반환
print("np.min(X) ==", np.min(X, axis=0)) # 각 열의 최소값을 모아서 벡터로 반환
print("np.max(X) ==", np.max(X, axis=1)) # 각 행의 최대값을 모아서 벡터로 반환
print("np.min(X) ==", np.min(X, axis=1)) # 각 행의 최소값을 모아서 벡터로 반환

print("np.argmax(X) ==", np.argmax(X, axis=0)) # 각 열의 최대값의 인덱스를 모아서 벡터로 반환
print("np.argmin(X) ==", np.argmin(X, axis=0)) # 각 열의 최소값의 인덱스를 모아서 벡터로 반환
print("np.argmax(X) ==", np.argmax(X, axis=1)) # 각 행의 최대값의 인덱스를 모아서 벡터로 반환
print("np.argmin(X) ==", np.argmin(X, axis=1)) # 각 행의 최소값의 인덱스를 모아서 벡터로 반환