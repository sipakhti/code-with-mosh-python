x = 10
y = 11

# z = x
# x = y
# y = z
# exactly the same as above
x, y = y, x
x, y = (y, x)

print("x", x)
print("y", y)

one = 1
two = 2
three = 3

one, two, three = three, two, one
print("One", one)
print("two", two)
print("three",three)