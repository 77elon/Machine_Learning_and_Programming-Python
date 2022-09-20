import numpy as np

def naive_relu(x):
    assert len(x.shape) ==2 #assert, shape?
    x = x.copy()
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            x[i, j] = max (x[i, j], 0)
            return x

a = np.array([[1, -2], [3, 4]])

result = naive_relu(a)
print(a)
print(result)
