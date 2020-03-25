import matplotlib.pyplot as plt
import numpy as np

# 绘制普通图像
x = np.linspace(-1, 1, 50)
y = 2 * x + 1
plt.plot(x, y)
plt.show()

# x = np.linspace(-1, 1, 50)
y1 = 2 * x + 1
# figure 1
plt.figure(num = 5, figsize = (4, 4))
plt.plot(x, y1)
plt.show()

# 绘制普通图像
y = x**2
plt.plot(x, y)
plt.show()