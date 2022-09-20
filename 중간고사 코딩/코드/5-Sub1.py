import numpy as np

def sel_multiply (x, y):
    assert len(x.shape) == 2
    assert len(y.shape) == 2
    
    x = x.copy()
    y = y.copy()
    for n in range(x.shape[0]):
        for m in range(y.shape[0]):
              x[n][m] *= y[n] #need if available ++
    return x
    
a = np.array([[1, 7], [2, 4]], dtype=int)
b = np.array([[3],[5]], dtype=int)

c = np.array([[1, 7], [2, 4]], dtype=int)
d = np.array([[3, 4], [5, 3]], dtype=int)
print(np.multiply(a, b))
print(sel_multiply(a, b))
    
#print(np.multiply(c, d))
#print(sel_multiply(c, d))
        

