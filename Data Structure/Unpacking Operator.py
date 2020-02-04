numbers = [1, 2, 3]
print(*numbers)
print(1, 2, 3)

values = list(range(5))
print(values)
print(*range(5), *"Hello")

values = [*range(5), * "Hello"]

first = [1, 2]
second = [3]
values = [*first, *second]
print(*values)

first = dict(x=1)
second = dict(x=10, y=2)
# incase of multiple values with similar keys, the last value will be used as in this case the value from the second dict
combined = {**first, **second, "Z":1}
print(combined)