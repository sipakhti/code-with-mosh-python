# Tuples is a read-only list
# tuples concatenation
point = (1,2)+(3,4)
print(type(point))
print(point)

# tuple repeatition
point = (1, 2) * 3
print(point)

# converting any list to tuple
point = tuple([1, 2])
print(point)

# converting any string to tuple
point = tuple("Hello World")
print(point)

# tuple indexing
point = (1, 2, 3)
print(point[0:2])
# tuple unpacking
x, y, z = point

if 10 in point:
    print("exist")