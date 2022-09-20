import numpy as np

a = np.arange(12)
b = a.reshape(3, 4) #Dimension Redefine 3x4
c = a.reshape(2, 3, 2) #3-Dimension

print(a)
print(b)
print(b.shape, b.ndim)
print(c)
print(c.shape, c.ndim)

