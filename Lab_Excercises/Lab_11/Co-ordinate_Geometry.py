import math as m
def distance(x1: int, x2: int, y1: int, y2: int):
    return m.sqrt((pow((x2 - x1), 2) + pow((y2 - y1), 2)))

def midpoint(x1: int, x2: int, y1: int, y2: int):
    return (x1 + x2) / 2, (y1 + y2) / 2

def slope(x1: int, x2: int, y1: int, y2: int):
    if x1 == x2:
        raise ValueError("Vertical - Undefined Slope")
    return (y2 - y1) / (x2 - x1)

x1 = int(input("Enter x1 : "))
x2 = int(input("Enter x2 : "))
y1 = int(input("Enter y1 : "))
y2 = int(input("Enter y2 : "))

print(f"Distance : {distance(x1,x2,y1,y2)}")
print("Midpoint : {0},{1}".format(*midpoint(x1,x2,y1,y2)))
try:
    slope(x1, x2, y1, y2)
except ValueError as error:
    print(error)
else:
    print(f"Midpoint : {slope(x1,x2,y1,y2)}")