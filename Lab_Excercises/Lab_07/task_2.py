# HCF
count = 0
factor1 = []
factor2 = []
number1 = int(input("Enter the first number:\n"))
number2 = int(input("Enter the second number:\n"))

while count < number1:
    count += 1
    if number1 % count == 0:
        factor1.append(count)

count = 0
while count < number2:
    count += 1
    if number2 % count == 0:
        factor2.append(count)



print("HCF:",sorted((set(factor1) & set(factor2)), reverse=True)[0])
