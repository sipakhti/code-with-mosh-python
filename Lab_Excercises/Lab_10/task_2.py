
def pyramid(user_input):
    if user_input > 2:
        pyramid(user_input - 1)
    for num in range(1, user_input+1):
        print(f"{' '*(user_input-num)}{'* '*num} ")




user_input = int(input("Enter a number: "))

pyramid(user_input)



