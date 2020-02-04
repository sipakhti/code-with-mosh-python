
x = int(input("Input the width of the diamond: "))
offset = int(input("OFFSET: "))
offset = " " * offset
count = x

for number in range(x):

    print(" " * (x - number), f" *{offset}" * number)

while count > 0:
    print(" " * (x - count), f" *{offset}" * count)
    count -= 1
