"#%%"
import numpy as np
import matplotlib.pyplot as plt

count = 100

popular = np.array([[982], [1042]])
move = np.array([[0.95, 0.03], [0.05, 0.97]])

s = [982]
g = [1042]


for i in range(count):
    popular = np.dot(move, popular)
    s.append(popular[0])
    g.append(popular[1])

plt.plot(s)
plt.plot(g)
plt.show()

print(s[100])
print(g[100])
