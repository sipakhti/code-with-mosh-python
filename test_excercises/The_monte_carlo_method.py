import random
import time
from math import pi , fabs
random.seed(time.time_ns())
shots = 100000
radius = 1
x, y = 0, 0
count = 0

Pi = 0
#while round(Pi, 3) != 3.142:
count = 0
avg = 0
for number in range(shots):
    random.seed(time.time_ns())
    x = fabs(random.uniform(-1.0, 1.0))
    #random.seed(time.thread_time_ns())
    y = fabs(random.uniform(-1.0, 1.0))
    #print(x**2 +y**2)
    if (x ** 2 + y ** 2 ) <= (1.0):
        count += 1
    Pi = (count / (number + 1)) * 4
    avg += Pi
    # if round(Pi, 3) == 3.142:
        # print(Pi, f"Total Number: {number}", f"Shots: {count}")
        
print(avg/shots)


print(round(avg/shots,2),round(pi,2))

