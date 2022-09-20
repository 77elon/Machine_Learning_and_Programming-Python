import numpy
import random

n=5000;
count=0.0;

for i in range(n):
    x=random.random();
    y=random.random();
    if(x*x+y*y<1):
      count+=1
      result = (4 * count) / n

print(result)