
dec = 0
binary = ""
error = True

while error:
    binary = input("Enter a BINARY sequence:\n")
    for bit in binary:
        if 0 <= int(bit) <= 1:
            error = False
        else:
            print("Wrong Binary Sequence. Only '1' and '0' are valid binary digits!\n")
            error = True

power = len(binary) - 1

for bit in binary:
    dec += int(bit) * pow(2, power)
    power -= 1


print(dec)
