# all sides equal
# if yes
# then square or rohumbus
#     all angles 90
#     if yes then square
#     if no then rohumbus
# if no
# then phomboid or rectangle
#     all angles 90
#     if yes rectangle
#     if no phomboid

from distutils import util

check1 = bool(util.strtobool(input("All are sides equal?\n")))
check2 = bool(util.strtobool(input("All are angles 90 degrees?\n")))

if check1 == True and check2 == True:
    print("It is a SQUARE!")
if check1 == True and check2 == False:
    print("It is a RHOMBUS!")
if check1 == False and check2 == True:
    print("It is a RECTANGLE!")
if check1 == False and check2 == False:
    print("It is a RHOMBOID!")
