import numpy as np

darts = 1000
i = 0
win = 0

for i in range(darts):

    x = np.random.random()
    y = np.random.random()
    z = (x**2 + y**2)**0.5

    if z <= 1:
        win +=1

value = 4 * win / darts

print('PI ={}'.format(value))
