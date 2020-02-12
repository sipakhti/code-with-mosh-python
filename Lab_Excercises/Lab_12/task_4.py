def factorial(number: int):
    for n in range(1, number):
        number *= n
    return number

def nCr(n: int, r: int):
    if n < 0 or r < 0:
        raise ValueError("\033[1;31m!!!Value of 'n' or 'r' cannot be less than '0'!!!\033[0m")
    if r > n:
        raise ValueError("\033[1;31m!!!Value of 'r' cannot be bigger than value of 'n'!!!\033[0m")
    if r == 0 and n == 0:
        ncr = 0
    else:
        ncr = (factorial(n) / (factorial(r) * factorial(n - r)))

    return ncr

def nPr(n: int, r: int):
    if n < 0 or r < 0:
        raise ValueError("\033[1;31m!!!Value of 'n' or 'r' cannot be less than '0'!!!\033[0m")
    if r > n:
        raise ValueError("\033[1;31m!!!Value of 'r' cannot be bigger than value of 'n'!!!\033[0m")
    if r == 0 and n == 0:
        npr = 0
    else:
        npr = factorial(n) / factorial(n - r)

    return npr

user_input = ""

while True:
    user_input = input("Operation to be performed: ")
    if user_input.lower() == "q":
        break
    val_n = int(input("Enter value of n: "))
    val_r = int(input("Enter value of r: "))

    if user_input.lower() == "c":
        try:
            print(f"{val_n}C{val_r} = {nCr(val_n,val_r)} ")
        except ValueError as error:
            print(error)
    elif user_input.lower() == "p":
        try:
            print(f"{val_n}P{val_r} = {nPr(val_n,val_r)} ")
        except ValueError as error:
            print(error)

print("Quiting Program.")


