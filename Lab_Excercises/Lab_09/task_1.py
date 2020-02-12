height = int(input("Enter Input = "))

for number in range(1, height + 1):
    print(" " * (height - number), (str(number) + " ") * number)
