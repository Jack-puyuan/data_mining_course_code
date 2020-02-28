import numpy as np
import matplotlib.pyplot as plt

A = np.mat('2,-1; -1,2')
B = np.mat('0,3').T
X = np.linalg.solve(A, B)
print(X)

Y = np.dot(B.T, np.linalg.inv(A))
print(Y)

x_VA1 = [0, 2]
y_VA1 = [0, -1]
x_VA2 = [0, -1]
y_VA2 = [0, 2]
scaled_x_VA1 = [0, 2]
scaled_y_VA1 = [0, -1]
scaled_x_VA2 = [0, 2]
scaled_y_VA2 = [3, -1]
combination_x = [0, 0]
combination_y = [0, 3]


plt.plot(x_VA1, y_VA1, 's-', color='r', label="VA1, The first column vector of A")  # s-:方形
plt.plot(x_VA2, y_VA2, 'o-', color='g', label="VA2, The second column vector of A")  # o-:圆形
plt.plot(scaled_x_VA1, scaled_y_VA1, 'o-', color='y', label="VA1 Scaled by x[0]")  # o-:圆形
plt.plot(scaled_x_VA2, scaled_y_VA2, 'o-', color='c', label="VA2 Scaled by x[1]")  # o-:圆形
plt.plot(combination_x, combination_y, 'o-', color='m', label="Linear Combination of VA1 and VA2")  # o-:圆形
# plt.xlabel("region length")  # 横坐标名字
# plt.ylabel("accuracy")  # 纵坐标名字
plt.legend(loc="best")  # 图例
plt.show()
