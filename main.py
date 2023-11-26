import numpy as np

no_darts = 1000
point = 0
i = 0

for i in range(no_darts):

    x = np.random.random()
    y = np.random.random()
    z = (x**2 + y**2)**0.5

    if z <= 1:
        point += 1

pi = 4 * point / no_darts

print('PI ={}'.format(pi))