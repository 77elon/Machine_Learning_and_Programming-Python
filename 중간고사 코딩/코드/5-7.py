import numpy as np
from numpy import linalg as LA

a = np.arange(9) - 4
print('a')
print('np.arange(9) - 4 : ',a)

b = a.reshape((3,3))
print('b')
print('a.reshape((3,3)) : \n',b)


print('LA.norm(a) : ',LA.norm(a))
print('LA.norm(b) : ',LA.norm(b))

print('LA.norm(b, ''fro'') : ',LA.norm(b, 'fro'))

print('LA.norm(a, np.inf) : ',LA.norm(a, np.inf))
print('LA.norm(b, np.inf) : ',LA.norm(b, np.inf))

print('LA.norm(a, -np.inf) : ',LA.norm(a, -np.inf))
print('LA.norm(b, -np.inf) : ',LA.norm(b, -np.inf))