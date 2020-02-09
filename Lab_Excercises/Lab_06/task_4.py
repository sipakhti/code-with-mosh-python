import math as m
a = int(input("Please enter first number:\n"))
b = int(input("Please enter second number:\n"))
c = int(input("Please enter third number number:\n"))

discriminant = (b ** 2) - (4 * a * c)

if discriminant == 0:
    print(f"Only one real root exists: {-(b/(a*2))}")
if discriminant > 0:
    print(
        f"Two distinct and real roots exist: {(-b)+(m.sqrt(discriminant)/(2*a))}  {(-b)-(m.sqrt(discriminant)/(2*a))} ")
if discriminant < 0:
    print(
        f"Two distinct and complex roots exist: {(-b/(2*a))+(m.sqrt(discriminant)/(2*a))}  {(-b/(2*a))-(m.sqrt(discriminant)/(2*a))}")
m.