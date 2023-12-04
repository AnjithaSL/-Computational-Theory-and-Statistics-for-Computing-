import numpy as num
import random

def sum_of_dice(number_of_attempt , dice , target ):
    count = 0

    for _ in range(number_of_attempt):
        throw = [random.randint(1, 6) for _ in range(dice)]

        if sum(throw) == target:
            count +=1

    pro = count / number_of_attempt

    return pro
  
number_of_attempt= 500
dice = 10
target= 32

value = sum_of_dice(number_of_attempt , dice , target )
print(f"Result is: {value}")

            