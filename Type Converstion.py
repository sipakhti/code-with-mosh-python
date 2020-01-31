x = input("x: ")
print(type(x))
y = int(x) + 1
print(type(x))
print(f"x: {x}, y: {y}")


# Falsy Values
# ""
# 0
# None
bool(0)
bool(1)
bool(-1)
bool("")
bool("False")