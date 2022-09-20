import numpy as np

def sel_multiply (x, y):
    assert len(x.shape) == 2
    assert len(y.shape) == 2
    
    x = x.copy()
    y = y.copy()
    z = []
    for n in range(x.shape[0]):
        result = 0
        for m in range(y.shape[0]):
              result += x[n][m] * y[m] #need if available ++
        z = np.append(z, result, axis = n - 1)
    return z
    
a = np.array([[1, 7], [2, 4]], dtype=int)
b = np.array([[3],[5]], dtype=int)

c = np.array([[1, 7], [2, 4]], dtype=int)
d = np.array([[3, 4], [5, 3]], dtype=int)
print(np.matmul(a, b))
print(sel_multiply(a, b))
    
print(np.matmul(c, d))
print(sel_multiply(c, d))
        
