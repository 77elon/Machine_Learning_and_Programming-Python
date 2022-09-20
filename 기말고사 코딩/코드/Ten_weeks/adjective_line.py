import numpy as np
import matplotlib.pyplot as plt

def calc(x, y):
	array = np.array([[1, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 0]])

	for m in range(4): #row
				array[m][1] = x[m]
				array[m][2] = (array[m][1]) ** 2
	
	plt.plot(x, y, 'bo')
	#array_transpose = np.transpose(array)
	print(array)

	result = np.linalg.inv(np.dot(np.transpose(array), array))
	result = np.dot(result, np.transpose(array))
	result = np.dot(result, y)
	result = np.reshape(result, (3, 1))
	print(result)

	x_range = np.arange(0, 5, 0.01)
	y_result = 0

	for i in range(len(result)):
		y_result += result[i] * x_range**i

	plt.plot(x_range, y_result)


# (1, 6), (2, 1), (3, 2), (4, 5)
x = np.array([1, 2, 3, 4])
y = np.array([6, 1, 2, 5])
calc(x, y)
