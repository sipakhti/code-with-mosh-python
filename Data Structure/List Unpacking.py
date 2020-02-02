numbers = [1, 2, 3, 4, 4, 9]
frist = numbers[0]
second = numbers[1]
third = numbers[2]


first, second, *other = numbers
print(first)
print(other)
first, *other, last = numbers
print(first, last)
print(other)