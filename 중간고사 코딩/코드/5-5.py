import numpy as np

def naive_vector_dot(x, y):
	assert len(x.shape) == 1
	assert len(y.shape) == 1
	assert x.shape[0] == y.shape[0] #Dimemsion Define

	z = 0.0
	for i in range(x.shape[0]):
		z+= x[i] * y[i]
		return z

a = np.array([1, 2, 3])
b = np.array([2, 3, 4])

c = np.dot(a, b)
print(c)

result = naive_vector_dot(a, b)
print(result)

