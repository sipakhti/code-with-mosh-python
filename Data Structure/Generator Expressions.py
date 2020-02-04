from sys import getsizeof
# when we use parenthesis around a comprehension expression we create a generator object which in way way easy on the memory instead of list and is iterable  
values = (x * 2 for x in range(100000))
print("generator", getsizeof(values))
# however we cannot find the length of the generator object
print(len(values))

values1 = [x * 2 for x in range(100000)]
print("list", getsizeof(values1))
