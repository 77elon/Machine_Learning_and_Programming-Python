import numpy as np
import matplotlib.pyplot as plt

rate = np.array([[64], [32], [4]])
poss = np.array([[0.7, 0.15, 0.3], [0.25, 0.8, 0.2], [0.05, 0.05, 0.5]]) #L, M, N

L = [rate[0]]
M = [rate[1]]
N = [rate[2]]

for iter in range(100):
    rate = np.dot(poss, rate)
    L.append(rate[0])
    M.append(rate[1])
    N.append(rate[2])

plt.plot(L)
plt.plot(M)
plt.plot(N)
plt.show()

print(rate)