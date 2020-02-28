import numpy as np
import matplotlib.pyplot as plt

n, p = 35, 0.7
# trial time is 70000
x = np.random.binomial(n, p, size=70000)
bins = np.arange(n +15)
# bins is x axis
plt.hist(x, bins=bins)

plt.title('Binomial Distribution with n={},p={}'.format(n, p))
plt.xlabel('number of successes')
plt.ylabel('(#Trial = 70000)')

plt.show()