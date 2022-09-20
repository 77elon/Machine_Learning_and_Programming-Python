import numpy

def calc(x):
    return 3 * x ** 2;

def Operator(n, m):
    tmp = 0.0
    tmp1 = 0.0
    for n in numpy.arange(n, m, 0.5):
        tmp = calc(n + 0.5)
        tmp1 += 0.5 * tmp
    return tmp1;

    
result = Operator(0.0, 1.0)

print(result)