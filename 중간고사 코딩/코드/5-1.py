import numpy as np

#dot product
print(np.dot(3, 4)) #12 1 Dimension

print(np.dot([2j, 3j], [2j, 3j]))

a = [[1, 0], [0, 1]]
b = [[4, 1], [2, 2]]

print(np.dot(a, b)) #identity matrix dot matrix == matrix

from numpy import linalg as LA

a=np.arange(9) - 4
print(a)
b=a.reshape((3,3)) #dimension ReDefine
print(b)

LA.norm(a)
LA.norm(b)

LA.norm(b, 'fro')

LA.norm(a, np.inf)
LA.norm(b, np.inf)

LA.norm(a, -np.inf)
LA.norm(b, -np.inf)

