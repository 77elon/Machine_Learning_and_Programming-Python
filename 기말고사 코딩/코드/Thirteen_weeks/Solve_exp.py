import random
import numpy as np
import scipy.special as sc

def Monte(n):
    previous_rand = [];
    start = 1000;
    for start in range(start, n):
        rand_range1 = random.random();
        rand_range2 = random.random();

        result_1 = 2 * rand_range1;
        result_2 = 2 * rand_range2; #x_1001

        if(result_2 / result_1 > random.random()):
            previous_rand.append(rand_range2); 
        else :
            previous_rand.append(rand_range1);
    return previous_rand;

def calc(n):
    return np.exp(n) / (2 * n);

random_list = Monte(1000000);
result = 0.0;
for i in range(random_list.__len__()):
    result += calc(random_list[i])
result /= random_list.__len__();

print(result)
print(sc.expi(1))  