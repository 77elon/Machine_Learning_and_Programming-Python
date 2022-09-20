import numpy as np

a = np.array([[1,0],[0,1]])
b = np.array([1,2])

print('a : \n',a)
print()
print('b : \n',b)
print()
print('np.matmul(a,b) : ',np.matmul(a,b))
print('np.matmul(b,a) : ',np.matmul(b,a))


c = np.arange(9.0).reshape((3,3))
d = np.arange(3.0)
print()
print('c : \n',c)
print()
print('d : \n',d)
print()
print('np.multiply(c,d) : \n',np.multiply(c,d))