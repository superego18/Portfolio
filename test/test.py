import numpy as np
from sklearn.linear_model import LinearRegression

X = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]])
y = np.array([17, 20, 35]).transpose

# # 첫번째 방법
# model = LinearRegression()
# model.fit(X,y)

# # 두번째 방법
# beta = np.linalg.pinv(X) @ y
# y_test = np.append(X) @ beta

X_ = np.array([np.append(x,[1]) for x in X])
print(X_)

print(np.linalg.pinv(X) @ y)
print(np.linalg.pinv(X_) @ y)