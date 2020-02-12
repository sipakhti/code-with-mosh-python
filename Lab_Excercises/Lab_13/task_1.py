from array import array


def avg(numbers: array):
    average = 0
    for x in numbers:
        average += x
    return average / len(numbers)


def lowest_highest(numbers):
    lowest = 0
    highest = 0
    for num in numbers:
        if num > highest:
            highest = num
        if num < lowest:
            lowest = num
    return lowest, highest


user_input = 0
numbers = array("i")

for x in range(15):
    numbers.append(int(input(f"Enter any number({x+1} of 15)")))

print(*numbers, sep="+", end=f" = {sum(numbers)}\n")
print(*numbers, sep="+", end=f" / {len(numbers)} = {avg(numbers)}\n")
print("Smallest element: {}\nLargest element: {}".format(*lowest_highest(numbers)))
