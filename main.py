import numpy as np

#number of dart throw
darts = 1000
i = 0
#number of hits to the circle
win = 0

for i in range(darts):

    x = np.random.random() #-1 to 1
    y = np.random.random() #-1 to 1
    z = (x**2 + y**2)**0.5 # search z using Pythagorean theorem

    if z <= 1:  #  z greater than 1 it hit to circle or not 
        win +=1

value = 4 * win / darts  # calculation of pi

print('PI ={}'.format(value))
