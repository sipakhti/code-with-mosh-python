from array import array
from random import choice , choices
numbers = [1,568468,2,6841,458,1284,3,84,1,84,48,3,68,184,1986]
place = True
temp = 0
print(numbers)
for i in range(1, len(numbers), 2):
    
    place = True
    while not (numbers[i] > numbers[i - 1] and numbers[i] > numbers[i + 1]):
        temp = choices([i + 1, i - 1])
        numbers[i], numbers[temp[0]] = numbers[temp[0]], numbers[i]


print(numbers)

