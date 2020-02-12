def power_funct(number: int or str, power: int or str):
    """Takes a number and its exponenent
        to calulate the answer"""
    number, power = int(number), int(power)
    if power == 1:
        return number

    return number * power_funct(number, power - 1)


user_input = input(
    "Enter the expression(X^Y), where X is the Base and Y is the exponent: ")

base, exponent = user_input.split("^")


print(power_funct(base, exponent))
