from os import system

import math as m

radius = 0
height = 0


print("The program computes the AREA and VOLUME of the following shapes:")
print("1: Sphere\n2: Cylinder\n3: Right Circular Cone")
shape = int(input(
    "Please enter the corresponding number of the desired shape to continue: "))
system("cls")
while 0 > shape > 3:
    shape = int(input(
        "Wrong Input\nValue must be from 1-3\nPlease enter the corresponding number of the desired shape to continue: "))
    system("cls")

if shape == 1:
    vol_area = input("press \"A\" for AREA or press \"V\" for VOLUME")
    if vol_area.lower() == "a":
        radius = int(input("enter the radius of the sphere: "))
        print(f"The Area of the the sphere is: {4*m.pi*radius**2}")
    elif vol_area.lower() == "v":
        radius = int(input("enter the radius of the sphere: "))
        print(f"The Volume of the sphere is: {(4/3)*m.pi*radius**2}")
    else:
        print("As you entered the incorrect option, the program must gracefully quit")
        exit
if shape == 2:
    vol_area = input("press \"A\" for AREA or press \"V\" for VOLUME")
    if vol_area.lower() == "a":
        radius = int(input("enter the radius of the Cylinder: "))
        height = int(input("enter the hieght of the Cylinder: "))
        print(
            f"The Area of the the Cylinder is: {(2*m.pi*radius*height)+(2*m.pi*radius**2)}")
    elif vol_area.lower() == "v":
        radius = int(input("enter the radius of the Cylinder: "))
        print(f"The Volume of the Cylinder is: {m.pi*radius**2*height}")
    else:
        print("As you entered the incorrect option, the program must gracefully quit")
        exit
if shape == 3:
    vol_area = input("press \"A\" for AREA or press \"V\" for VOLUME")
    if vol_area.lower() == "a":
        radius = int(input("enter the radius of the Cone: "))
        height = int(input("enter the height if the Cone: "))
        print(
            f"The Area of the the Cone is: {m.pi*radius+(m.pi * radius * m.sqrt(radius ** 2 * height ** 2))}")
    elif vol_area.lower() == "v":
        radius = int(input("enter the radius of the Cone: "))
        height = int(input("enter the radius of the Cone: "))
        print(f"The Volume of the Cone is: {(m.pi*radius**2*height/3)}")
    else:
        print("As you entered the incorrect option, the program must gracefully quit")
        exit
